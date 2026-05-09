# RepoMind

AI-powered repository intelligence and developer automation platform.

RepoMind allows developers to chat with any GitHub repository using Retrieval-Augmented Generation (RAG), semantic search, and streaming AI responses.

---

## Frontend

[https://repo-mind-gray.vercel.app](https://repo-mind-gray.vercel.app)

## Backend API

[https://repo-mind-production.up.railway.app](https://repo-mind-production.up.railway.app)

---

# Features

* AI-powered repository understanding
* Dynamic GitHub repository indexing
* Semantic code search using embeddings
* Retrieval-Augmented Generation (RAG)
* Streaming ChatGPT-style AI responses
* Explainable source attribution
* Full-stack React + FastAPI architecture
* Cloud deployment on Vercel + Railway
* Production-ready environment configuration

---

# Architecture

```text
Frontend (React + Vite)
        ↓
FastAPI Backend (Railway)
        ↓
Semantic Search + RAG Pipeline
        ↓
OpenAI Embeddings + LLM APIs
```

---

# Tech Stack

## Frontend

* React
* TypeScript
* Vite
* Axios
* React Markdown
* React Hot Toast

## Backend

* FastAPI
* Python
* OpenAI API
* NumPy
* Uvicorn

## AI / RAG

* OpenAI Embeddings (`text-embedding-3-small`)
* Semantic similarity search
* Retrieval-Augmented Generation (RAG)
* Streaming AI responses

## Deployment

* Vercel
* Railway

---

# How RepoMind Works

## 1. Repository Indexing

Users provide a GitHub repository URL.

RepoMind:

* Downloads repository source code
* Extracts supported files
* Splits code into chunks
* Generates embeddings
* Stores vectors for semantic retrieval

---

## 2. Semantic Retrieval

When a user asks a question:

* The question is converted into an embedding
* Similar code chunks are retrieved using cosine similarity
* Most relevant repository context is selected

---

## 3. AI-Powered Answers

Retrieved repository context is passed into an LLM prompt.

RepoMind then:

* Generates technical explanations
* Streams responses in real-time
* Returns source attribution with similarity scores

---

# Supported File Types

RepoMind currently indexes:

* Python (`.py`)
* JavaScript (`.js`)
* TypeScript (`.ts`, `.tsx`)
* Java (`.java`)
* Go (`.go`)
* Markdown (`.md`)
* JSON (`.json`)
* YAML (`.yaml`, `.yml`)

Ignored directories:

* `venv`
* `node_modules`
* `.git`
* `__pycache__`
* `dist`
* `build`

---

# Local Development Setup

## Clone Repository

```bash
git clone https://github.com/IamOmkarG/repo-mind.git

cd repo-mind
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create:

```text
.env
```

Add:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# Frontend Setup

```bash
cd frontend
```

## Install Dependencies

```bash
npm install
```

---

## Configure Frontend Environment

Create:

```text
frontend/.env
```

Add:

```env
VITE_API_URL=http://localhost:8000
```

---

## Run Frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# API Endpoints

## Health Check

```http
GET /
```

---

## Index Repository

```http
POST /index
```

### Request

```json
{
  "repo_url": "https://github.com/pallets/flask"
}
```

---

## Ask Repository Question

```http
POST /ask-stream
```

### Request

```json
{
  "question": "How does Flask routing work?"
}
```

---

# Example Questions

## Flask

* How does Flask routing work?
* How are requests handled?
* What is app context?

## FastAPI

* How does dependency injection work?
* How are routes registered?
* How does request validation work?

## General

* What does this repository do?
* Explain the architecture.
* How is authentication implemented?
* How does semantic search work?

---

# Project Structure

```text
repo-mind/
│
├── backend/
│   ├── api/
│   ├── embeddings/
│   ├── ingestion/
│   ├── models/
│   ├── services/
│   ├── storage/
│   └── vectorstore/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── services/
│
├── tests/
├── requirements.txt
└── README.md
```

---

# Future Improvements

* Vector database integration (Pinecone / Weaviate)
* Code-aware chunking
* Hybrid retrieval + reranking
* Repository architecture visualization
* Multi-repository memory
* Authentication and saved chats
* Background indexing workers
* Repository summarization
* Dependency graph analysis

---

# Production Challenges Solved

During deployment, several real-world production engineering challenges were solved:

* CORS configuration issues
* Railway networking configuration
* Environment variable management
* Cloud filesystem limitations
* Streaming response deployment
* Missing dependency debugging
* Runtime path creation
* Frontend/backend production networking

---

# Why RepoMind?

Modern repositories are becoming increasingly complex.

RepoMind helps developers:

* Understand unfamiliar codebases faster
* Explore repository architecture conversationally
* Retrieve implementation details instantly
* Improve onboarding experience
* Reduce manual code exploration time

---

# Author

Omkar Gunge

* Software Engineer @ Amazon
* AI Systems & Developer Tooling Enthusiast

GitHub:
[https://github.com/IamOmkarG](https://github.com/IamOmkarG)

---
