# 🚀 AI SaaS Chatbot Platform

Production-ready AI SaaS backend built with FastAPI, OpenAI, RAG architecture, JWT authentication, RBAC, analytics, and multi-tenant support.

---

## 📌 Features

## 🤖 AI Chat System

- OpenAI GPT integration
- Retrieval-Augmented Generation (RAG)
- Context-aware responses
- Conversation memory
- Intelligent document retrieval

---

## 📚 Knowledge Base

- PDF upload support
- TXT upload support
- Vector embeddings
- FAISS vector database
- Semantic search

---

## 🔐 Authentication & Security

- JWT Authentication
- OAuth2 Password Flow
- Password hashing with bcrypt
- Role-Based Access Control (RBAC)
- Protected API endpoints

---

## 👥 Multi-Tenant SaaS Architecture

- User isolation
- Session-based memory
- Per-user chat history
- Tenant-aware caching

---

## 📊 Analytics Dashboard

- Request tracking
- Response time monitoring
- Recent activity logs
- Category analytics

---

## 🛠️ Tech Stack

## Backend

- FastAPI
- Python 3.12
- SQLAlchemy
- PostgreSQL

## AI / ML

- OpenAI API
- Embeddings
- FAISS Vector Database

## Authentication

- JWT
- OAuth2
- Passlib
- bcrypt

## DevOps / Tools

- Uvicorn
- Pydantic
- Git
- GitHub

---

## 📂 Project Structure

```bash
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── uploads/
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

cd backend
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=postgresql://postgres:password@localhost/ai_chatbot

SECRET_KEY=your_generated_secret_key

ALGORITHM=HS256

APP_NAME=AI Chatbot

DEBUG=True
```

---

## 🗄️ Database Setup

Make sure PostgreSQL is running.

Create database:

```sql
CREATE DATABASE ai_chatbot;
```

---

## ▶️ Run Application

```bash
python -m uvicorn app.main:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication Flow

## Register

```http
POST /auth/register
```

---

## Login

```http
POST /auth/login
```

Returns JWT token.

---

## Authorize

Use Swagger UI `Authorize` button and paste token.

---

## 📄 File Upload

Supports:

- PDF
- TXT

Endpoint:

```http
POST /upload
```

---

## 🧠 RAG Pipeline

1. Upload document
2. Split into chunks
3. Generate embeddings
4. Store in FAISS
5. Retrieve relevant context
6. Generate AI response

---

## 📊 Admin Endpoints

## Summary

```http
GET /admin/summary
```

## Recent Activity

```http
GET /admin/recent
```

---

## 🔒 RBAC Roles

## User

- Chat access
- Upload documents

## Admin

- Analytics access
- Vector DB management
- System monitoring

---

## 🚀 Future Improvements

- React Frontend
- Redis Caching
- Pinecone Vector DB
- Docker Deployment
- CI/CD Pipeline
- Streaming Responses
- Multi-file ingestion
- Stripe Billing
- SaaS Subscription System

---

## 🧪 API Testing

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 📈 Current Architecture

- FastAPI REST API
- JWT Authentication
- RAG AI Pipeline
- FAISS Semantic Search
- PostgreSQL Persistence
- Multi-Tenant SaaS Structure

---

## 👨‍💻 Author

Built by Ugboma Omoefe Ugboma

Master's Student in Artificial Intelligence  
Machine Learning Engineer & Full-Stack Developer

---

## ⭐ License

MIT License