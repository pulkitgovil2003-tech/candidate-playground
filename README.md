# Candidate Playground

A minimal full-stack playground that stores and exposes my candidate profile via a REST API and a basic frontend UI.

---

## 🧱 Architecture

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: Plain HTML + JavaScript
- **Hosting**:
  - Backend: Render Web Service
  - Frontend: Render Static Site

---

## 🌐 Live URLs

- **Backend API**:  
  https://candidate-playground-gqa9.onrender.com

- **Frontend UI**:  
  https://candidate-playground-1.onrender.com

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/health` | Liveness check |
| GET | `/profile` | Fetch candidate profile |
| GET | `/projects` | List all projects |
| GET | `/search?q=` | Search projects |

---

## 🗄 Database Schema

### `profile`
- id
- name
- email
- education
- github
- linkedin
- portfolio

### `skills`
- id
- name

### `projects`
- id
- title
- description
- link

---

## ⚙ Local Setup

```bash
git clone https://github.com/pulkitgovil2003-tech/candidate-playground.git
cd backend

python -m venv venv
venv\Scripts\activate
pip install flask flask-cors

python app.py
