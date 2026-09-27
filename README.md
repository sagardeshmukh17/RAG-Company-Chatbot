# 🏢 Company RAG Chatbot

A simple **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **OpenAI**, and **ChromaDB**.  
It allows you to ask questions about company documents and get context‑based answers.

---

## 🚀 Features
- Embeds company documents into **ChromaDB** for vector search
- Retrieves relevant context for queries
- Uses **OpenAI GPT models** to generate answers
- Simple **Streamlit UI** for interaction

---

## 📂 Project Structure
03-RAG-App/
│── ingest.py        # Reads company.txt, generates embeddings, stores in ChromaDB
│── rag.py           # Query function: retrieves context + calls OpenAI
│── app.py           # Streamlit UI
│── documents/
│    └── company.txt # Company policies and info
│── requirements.txt # Dependencies
│── .env             # API key (ignored in git)


---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/sagardeshmukh17/RAG-Company-Chatbot.git
   cd RAG-Company-Chatbot

2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Add your OpenAI API key in .env
OPENAI_API_KEY=your_api_key_here
python ingest.py
streamlit run app.py
