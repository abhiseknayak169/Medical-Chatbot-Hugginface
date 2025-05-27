🩺 Medical Guidelines Chatbot
A conversational assistant that answers questions from uploaded medical PDF guidelines using LangChain, Hugging Face LLMs, FAISS vectorstore, and Gradio UI — with memory and source chunk traceability.

✅ Upload any clinical guideline
✅ Ask multi-turn questions
✅ Answers are grounded in PDF content only
✅ Cites source chunks for transparency
✅ No hallucinations — includes fallback logic

🔧 Features
✅ Upload PDF guidelines dynamically

✅ Automatically chunk, embed, and store in FAISS

✅ Conversational memory (ConversationBufferMemory)

✅ Hugging Face Inference API (Zephyr/Mistral/etc.)

✅ Highlights source context chunks used in answers

✅ Built with Gradio for a clean, chat-like UI

✅ Safe fallback: “This information is not available in the current guidelines.”

🚀 Getting Started
1. Clone the repo
bash
Copy
Edit
git clone repository
cd medical-guidelines-chatbot
2. Create a .env file
bash
Copy
Edit
touch .env
Add your Hugging Face token to the .env file:

env
Copy
Edit
HF_TOKEN=your_huggingface_token_here
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the chatbot
bash
Copy
Edit
python app.py
Then open your browser at: http://localhost:8080

📄 Project Structure
bash
Copy
Edit
.
├── app.py                    # Gradio app with ConversationalRetrievalChain
├── requirements.txt
├── .env                      # Your Hugging Face token
├── src/
│   ├── helper.py             # Embedding model loader
│   └── prompt.py             # Custom prompts for rephrasing & answers
└── vectorstore/              # Temporary FAISS DBs (optional)
🧠 Example Usage
Upload a file like ICMR_Treatment_Guidelines.pdf and ask:

plaintext
Copy
Edit
💬 What is hospital acquired infection?
💬 What organisms are responsible?
💬 What is the treatment for complicated intra-abdominal infections?
💬 What did I ask earlier?
📦 To Deploy on Hugging Face Spaces
If you want a public link:

Add share=True to demo.launch(...)

Push this repo to Hugging Face with Space type Gradio (Python)

🙏 Disclaimer
This is for educational purposes only and not medical advice.
Always consult a healthcare professional before acting on any information.

