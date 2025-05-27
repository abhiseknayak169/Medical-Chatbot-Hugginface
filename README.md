# 🩺 Medical Guidelines Chatbot

This is an AI-powered chatbot that answers questions from uploaded medical guideline PDFs using Hugging Face LLMs, LangChain, FAISS vector search, and Gradio. It supports conversational memory, answer traceability, and accurate grounding in source content.

---

## 🚀 Features

* 📄 Upload your own medical guideline PDF (e.g. ICMR, WHO, NACO)
* 🔍 Ask clinical questions and receive fact-grounded answers
* 🧠 Conversation memory using LangChain's `ConversationBufferMemory`
* 📚 FAISS vector store for fast document retrieval
* ✅ Source chunk display for transparency
* 🤖 Hugging Face model support (tested with Zephyr 7B)
* 🧾 Safe fallback: "This information is not available in the current guidelines"

---

## 🧑‍💻 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/abhiseknayak169/Medical-Chatbot-Hugginface.git
cd medical-chatbot
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Add your Hugging Face token

Create a `.env` file:

```bash
echo "HF_TOKEN=your_token_here" > .env
```

### 4. Run the app

```bash
python app.py
```

Then open [http://localhost:8080](http://localhost:7860)

---

## 🧾 Folder Structure

```
medical-chatbot/
├── app.py                 # Gradio app with LangChain logic
├── requirements.txt       # All dependencies
├── .env                   # Hugging Face API token
├── src/
│   ├── helper.py          # Embedding model loader
│   └── prompt.py          # Prompt templates for answering and question rewriting
```

---

## 📋 Example Usage

1. Upload a PDF like `ICMR_Treatment_Guidelines.pdf`
2. Ask:

   * What is Hospital Acquired Infection?
   * What are the causes of HAI?
   * How is it diagnosed?
3. See source chunks shown with the answer.

---

## ✅ Safety Note

> *This tool is for **educational purposes only** and should **not** be used as a substitute for professional medical advice.*

---

## 🌐 Deploy to Hugging Face Spaces

1. Push this code to a public repo
2. Create a new **Gradio (Python)** Space
3. Add your Hugging Face token as a secret `HF_TOKEN`
4. Paste your app code and hit Deploy

---

## 🧠 Credits

* [LangChain](https://python.langchain.com/)
* [Gradio](https://gradio.app/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [ICMR, NACO, WHO PDFs](https://www.icmr.gov.in/)

---

Need help? Open an issue or ping me on Hugging Face!
