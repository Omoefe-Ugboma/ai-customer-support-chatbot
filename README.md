# 🚀 AI SaaS Platform — Enterprise AI Assistant

## A production-style AI SaaS platform built with:

* FastAPI
* React + Vite
* PostgreSQL
* OpenAI
* JWT Authentication
* Vector Search (FAISS)
* Streaming AI Responses
* Persistent Chat Threads
* Analytics Dashboard
* Role-Based Authentication
* Retrieval-Augmented Generation (RAG)

* This project demonstrates modern full-stack AI engineering architecture similar to ChatGPT, Claude, and Gemini-style systems.

## 📌 Features

✅ Authentication & Authorization
JWT Authentication
Secure Login & Registration
Persistent Sessions
Role-Based Access Control (Admin/User)
Protected Routes
Token-Based API Security

✅ AI Chat System
Real-time Streaming AI Responses
ChatGPT-style Conversation UI
Persistent Chat History
Multi-thread Conversations
Conversation Restore
Conversation Rename/Delete
Typing Indicators
Context-Aware Memory

✅ Retrieval-Augmented Generation (RAG)
Upload Documents
Semantic Search
Vector Embeddings
FAISS Vector Store
Context Retrieval
AI Answers From Uploaded Documents

✅ Admin Dashboard
Request Analytics
Average Response Time
Recent Interactions
User Activity Monitoring
AI Usage Statistics

✅ Frontend Features
Modern Responsive UI
Sidebar Navigation
Protected Pages
Streaming Responses
TailwindCSS Styling
ChatGPT-inspired UX
Smooth Navigation
Persistent Authentication

## 🏗️ System Architecture

Frontend (React + Vite)
        ↓
FastAPI Backend
        ↓
Authentication Layer (JWT)
        ↓
AI Services Layer
        ↓
OpenAI + Vector Store (FAISS)
        ↓
PostgreSQL Database

## 🧠 Tech Stack
Frontend
React
Vite
TailwindCSS
Axios
React Router
React Hook Form
Lucide React

Backend
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
JWT (python-jose)
Passlib
OpenAI SDK
FAISS
Uvicorn

## 📂 Project Structure

ai-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── services/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md

## ⚙️ Backend Setup

1️⃣   Clone Repository
git clone https://github.com/yourusername/ai-saas-platform.git
cd ai-saas-platform

2️⃣   Setup Virtual Environment
cd backend

python -m venv venv
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate

3️⃣   Install Dependencies
pip install -r requirements.txt

4️⃣   Configure Environment Variables
Create:
backend/.env
Example:
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=postgresql://postgres:password@localhost/ai_chatbot

SECRET_KEY=your_super_secret_key

ALGORITHM=HS256

APP_NAME=AI SaaS Platform

DEBUG=True

5️⃣   Run Backend
python -m uvicorn app.main:app --reload
Backend URL:
http://127.0.0.1:8000
Swagger Docs:
http://127.0.0.1:8000/docs

💻 Frontend Setup
1️⃣   Install Dependencies
cd frontend
npm install

2️⃣   Start Frontend
npm run dev
Frontend URL:
http://localhost:5173

## 🔐 Authentication Flow

User Login/Register
        ↓
FastAPI Auth Routes
        ↓
JWT Token Generation
        ↓
Frontend Stores Token
        ↓
Protected Route Access

## 🤖 AI Streaming Flow

User Message
        ↓
FastAPI Streaming Endpoint
        ↓
OpenAI Streaming Response
        ↓
React Incremental Rendering
        ↓
Live AI Response

## 📚 RAG Workflow

Upload Document
        ↓
Generate Embeddings
        ↓
Store in FAISS
        ↓
Semantic Search
        ↓
Inject Context into Prompt
        ↓
AI Generates Accurate Response

## 📊 Analytics Features

Total Requests
Average Response Time
User Interactions
Recent Conversations
Request Categories
AI Usage Monitoring

## 🔒 Security Features

JWT Authentication
Password Hashing (bcrypt)
Protected Routes
Environment Variables
SQLAlchemy ORM Protection
Token-Based Authorization
Secure API Access

## 🧪 API Endpoints

Authentication
POST /auth/register
POST /auth/login

Chat
POST /chat
POST /chat/stream

Threads
GET /threads
POST /threads
PUT /threads/{id}
DELETE /threads/{id}

Uploads
POST /upload
POST /add-documents
POST /reset-documents
POST /clear-cache

Analytics
GET /admin/summary
GET /admin/recent

## 🧑‍💻 Engineering Highlights

This project demonstrates:
AI Engineering
Full-Stack Engineering
Enterprise Architecture
Secure Authentication
Production API Design
React State Management
Streaming Architectures
Vector Search Systems
Database Relationships
Clean Code Organization
Scalable Service Layers
Real-time AI Applications

## 🧠 Skills Demonstrated

Python
FastAPI
React
PostgreSQL
SQLAlchemy
AI Engineering
OpenAI APIs
Vector Databases
JWT Authentication
REST APIs
Streaming Architectures
RAG Systems
State Management
TailwindCSS
Full-Stack Development
Enterprise Software Design

## 🏆 Why This Project Matters To Me

This project demonstrates the ability to:
Build scalable AI applications
Design modern SaaS architectures
Integrate LLMs into production systems
Create real-time AI experiences
Implement secure authentication systems
Engineer persistent AI memory systems
Develop enterprise-grade frontend systems
Build AI-powered products end-to-end

## 📄 License

MIT License

## 🙌 Acknowledgements

OpenAI
FastAPI
React
PostgreSQL
FAISS
TailwindCSS
Vite

## 📸 Application Screenshots

## 🔐 Login Page

![Login Page](screenshots/login-page.png)

---

## 📝 Register Page

![Register Page](screenshots/register-page.png)

---

## 🤖 AI Chat Interface

![Chat Interface](screenshots/chat-interface.png)

---

## ⚡ Streaming AI Responses

![Streaming Responses](screenshots/streaming-response.png)

---

## 📤 Upload System

![Upload System](screenshots/upload-system.png)

---

## 📊 Analytics Dashboard

![Analytics Dashboard](screenshots/analytics-dashboard.png)

---

## 🧠 Conversation Sidebar

![Conversation Sidebar](screenshots/conversation-view.png)

---

## 💾 Dashboard Screen

![Persistent Threads](screenshots/Dashboard_screen.png)

---

## 💾 Swagger Docs 

![Persistent Threads](screenshots/swagger-docs.png)

---

## 📚 Chat Persistence 

![Swagger Docs](screenshots/persistent-threads.png)


---

## 📚 Posgres Interface with Chat output

![Swagger Docs](screenshots/Posgresql_Screenshot.png)


👨‍💻 Author
Developed by Ugboma Omoefe Ugboma
AI Engineer | Full-Stack Developer | Machine Learning Enthusiast
