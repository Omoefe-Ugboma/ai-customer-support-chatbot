# 🤖 AI Customer Support Chatbot (RAG System)

An AI-powered customer support system that uses Large Language Models (LLMs) to understand user queries, retrieve relevant knowledge, and generate intelligent responses.

---

## 🚀 Features

* 💬 Chat interface (like ChatGPT)
* 🧠 Context-aware responses
* 🔎 Retrieval-Augmented Generation (RAG)
* 📄 Document-based knowledge (PDF, TXT)
* 🗂 Conversation memory
* 📊 Admin dashboard (coming soon)

---

## 🧱 Tech Stack

### Backend

* FastAPI
* OpenAI API (LLM)
* Python

### Frontend

* React (Vite)
* Tailwind CSS

### AI / ML

* Embeddings (coming)
* Vector DB (FAISS / Pinecone - upcoming)
* RAG architecture

---

## 📦 Project Structure

```
ai-chatbot/
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│
├── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### 🎨 Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🔑 Environment Variables

Create `.env` in backend:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🧪 API Docs

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Current Status

## AI Chatbot (LLM) ✔ v0.1

* Basic AI chat implemented
* Basic AI Chat
* Clean architecture
* API integration

## ✅ Version v0.2— Memory System (Context)

* Persistent chat history using PostgreSQL
* Context-aware responses using conversation memory
* Multi-turn AI conversations

## 🚀 Version v0.3 — RAG System (Knowledge-Based AI)

* Implemented embeddings using OpenAI API
* Integrated FAISS vector database for semantic search
* Built document ingestion pipeline
* Enabled Retrieval-Augmented Generation (RAG)
* Chatbot now answers based on custom knowledge base

## 🚀 Version v0.4 — Document Upload (PDF → RAG)

* File upload support (PDF, TXT)
* Text extraction using PyPDF2
* Chunk-based document processing
* Integration with FAISS vector database
* AI can now answer questions from uploaded documents

## 🚀 Version v0.5 — Advanced RAG (Production-Level)

* Top-K retrieval with similarity scoring
* Re-ranking layer for improved relevance
* Context cleaning to remove duplicates
* Prompt optimization to reduce hallucination
* Optional caching for performance
* Enhanced response accuracy and reliability

* Memory system
* Vector search (FAISS)
* Document upload (RAG)

---

## 📌 Author

Omoefe Joseph Ugboma
MSc Artificial Intelligence — University of Mauritius
