# 🧠 TatvaMind AI Career Engine

### High-Level Architecture & Development Roadmap

---

## 📁 Project Structure

```bash

tatvamind-ai-career-engine/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── config.py # Environment variables & settings
│ │ │
│ │ ├── api/ # API layer (routes/endpoints)
│ │ │ └── routes.py
│ │ │
│ │ ├── services/ # 🔥 Core business logic (brain of system)
│ │ │ ├── parser.py # Resume & JD text extraction
│ │ │ ├── embeddings.py # Text → vector embeddings
│ │ │ ├── rag_pipeline.py # Retrieval + generation pipeline
│ │ │ ├── scorer.py # Match scoring logic
│ │ │ └── llm.py # LLM interaction layer
│ │ │
│ │ ├── models/ # Data schemas (Pydantic)
│ │ │ └── schema.py
│ │ │
│ │ ├── db/ # Data & vector storage layer
│ │ │ ├── chroma_client.py # Vector DB connection
│ │ │ └── storage.py # Storage abstraction
│ │ │
│ │ ├── utils/ # Helper utilities
│ │ │ ├── chunking.py # Text splitting logic
│ │ │ └── keywords.py # Keyword extraction
│ │ │
│ │ └── core/ # Shared constants/config
│ │ └── constants.py
│ │
│ ├── tests/ # Unit & integration tests
│ │
│ ├── requirements.txt
│ ├── Dockerfile
│ └── docker-compose.yml
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── app/ # Next.js pages (routing)
│ │ ├── components/ # Reusable UI components
│ │ ├── lib/ # API calls & helpers
│ │ └── styles/ # Styling (Tailwind / CSS)
│ │
│ ├── package.json
│ └── next.config.js
│
├── deployment/
│ ├── nginx.conf # Reverse proxy config
│ ├── gcp-setup.md # Deployment guide (GCP)
│ └── scripts/ # Automation scripts
│
├── .env # Environment variables
├── .gitignore
└── README.md

```

---

## 🧠 Folder Responsibilities

### 🔹 `backend/app/services/` (Core Engine)

This is the **brain of the system**.

- Handles parsing, embeddings, RAG logic, scoring, and LLM interaction
- Most critical part of the entire product

---

### 🔹 `backend/app/api/` (Interface Layer)

- Defines API endpoints
- Connects frontend with backend logic
- Keeps routing separate from logic

---

### 🔹 `backend/app/db/` (Memory Layer)

- Manages vector database (Chroma)
- Handles storage abstraction
- Future: integrate PostgreSQL for user data

---

### 🔹 `backend/app/utils/` (Support Functions)

- Chunking logic
- Keyword extraction
- Reusable helper utilities

---

### 🔹 `backend/app/models/` (Data Contracts)

- Request/response schemas
- Ensures clean and structured API communication

---

### 🔹 `frontend/` (Presentation Layer)

- User interface (Next.js)
- Handles user interaction
- Consumes backend APIs

---

### 🔹 `deployment/` (Production Layer)

- Nginx configuration
- GCP setup instructions
- Deployment scripts

---

## 🚀 Development Phases

---

### 🟢 Phase 1 — MVP (Core Functionality)

**Goal:** Validate idea quickly

- Resume text extraction (PDF/DOCX)
- Job Description input
- LLM-based analysis
- Output:
  - Match score
  - Missing keywords
  - Suggestions

✅ No RAG  
✅ No vector DB  
✅ Focus on working prototype

---

### 🟡 Phase 2 — RAG Integration

**Goal:** Improve intelligence & accuracy

- Text chunking
- Embedding generation
- Vector database (Chroma)
- Semantic retrieval of relevant resume sections
- Context-aware LLM prompts

---

### 🔵 Phase 3 — Scoring Engine

**Goal:** Make results more reliable

- Keyword match percentage
- Semantic similarity scoring
- Section-wise evaluation (skills, experience, projects)
- Weighted scoring system

---

### 🟣 Phase 4 — API & System Design

**Goal:** Make it usable as a service

- FastAPI endpoints
- Structured JSON responses
- Error handling
- Modular service architecture

---

### 🟠 Phase 5 — Frontend Development

**Goal:** Create user-facing product

- Resume upload UI
- JD input interface
- Results dashboard
- Clean, responsive design

---

### 🔴 Phase 6 — Deployment (Global Access)

**Goal:** Launch to real users

- Docker containerization
- GCP Compute Engine deployment
- Nginx reverse proxy
- Domain + SSL (HTTPS)

---

### 🟤 Phase 7 — Monetization & Scaling

**Goal:** Generate revenue

- Authentication system
- Payment integration (Stripe/Razorpay)
- Usage limits (free vs paid)
- Analytics dashboard

---

## 💡 Key Philosophy

> Build → Validate → Improve → Scale

- Start simple (LLM only)
- Add RAG when needed
- Focus on real user value, not complexity

---

## 🎯 Final Goal

A **production-ready AI system** that:

- Helps users improve resumes
- Increases job success rate
- Generates real revenue under **TatvaMind Labs**
