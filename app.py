# app.py
import gradio as gr
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from src.helper import get_embedding_model
from src.prompt import CUSTOM_PROMPT_TEMPLATE as CUSTOM_PROMPT_TEXT, CONDENSE_QUESTION_PROMPT as CONDENSE_PROMPT_TEXT

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")
HUGGINGFACE_REPO_ID = "HuggingFaceH4/zephyr-7b-beta"

embedding_model = get_embedding_model()
qa_chain = None
memory = None

CONDENSE_QUESTION_PROMPT = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=CONDENSE_PROMPT_TEXT
)

CUSTOM_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["context", "question"],
    template=CUSTOM_PROMPT_TEXT
)

def load_llm(repo_id):
    return HuggingFaceEndpoint(
        repo_id=repo_id,
        temperature=0.5,
        huggingfacehub_api_token=HF_TOKEN,
        max_new_tokens=512
    )

def process_pdf_and_create_chain(pdf_file):
    global qa_chain, memory
    loader = PyPDFLoader(pdf_file.name)
    pages = loader.load_and_split()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(pages)

    db = FAISS.from_documents(docs, embedding_model)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        input_key="question",
        output_key="answer",
        return_messages=True
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=load_llm(HUGGINGFACE_REPO_ID),
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        return_source_documents=True,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
        combine_docs_chain_kwargs={"prompt": CUSTOM_PROMPT_TEMPLATE}
    )

    return "✅ File processed. You can now chat with memory."

def get_response(message):
    if qa_chain is None:
        return "⚠️ Please upload a PDF first.", []

    response = qa_chain.invoke({"question": message})
    answer = response.get("answer", "").strip()

    if not response.get("source_documents"):
        return "🟡 This information is not available in the current guidelines.", []

    source_chunks = []
    for i, doc in enumerate(response["source_documents"]):
        page = doc.metadata.get("page", "N/A")
        source = doc.metadata.get("source", "PDF")
        text = doc.page_content.strip().replace("\n", " ")
        source_chunks.append(f"**{source} — Page {page}:** {text[:500]}{'...' if len(text) > 500 else ''}")

    return answer, source_chunks

with gr.Blocks() as demo:
    gr.Markdown("## 🩺 Medical Guidelines Assistant\n\n_Disclaimer: This is for educational purposes only and not medical advice._")

    with gr.Row():
        file_upload = gr.File(label="📄 Upload a Medical Guidelines PDF", file_types=[".pdf"])
        upload_status = gr.Textbox(label="Upload Status", interactive=False)

    file_upload.change(fn=process_pdf_and_create_chain, inputs=file_upload, outputs=upload_status)

    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(label="Ask a question", placeholder="e.g. What is the treatment for cellulitis?")
    gr.Markdown("### 🔍 Retrieved Chunks")
    source_view = gr.Markdown("")
    clear = gr.Button("Clear")

    def user_submit(user_message, chat_history):
        answer, chunks = get_response(user_message)
        chat_history.append((user_message, answer))
        joined_chunks = "\n\n".join(chunks)
        return "", chat_history, joined_chunks

    def reset_memory():
        if memory:
            memory.clear()
        return [], ""

    msg.submit(user_submit, [msg, chatbot], [msg, chatbot, source_view])
    clear.click(reset_memory, None, [chatbot, source_view], queue=False)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080, share=True)