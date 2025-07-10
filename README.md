![Backend Tests](https://github.com/AtharvaRasal/Django-react/actions/workflows/backend-tests.yml/badge.svg)
[![codecov](https://codecov.io/github/AtharvaRasal/Django-react/graph/badge.svg?token=ZJLQOPUB2R)](https://codecov.io/github/AtharvaRasal/Django-react)

# 🗒️ Notes Management System

A full-stack **Notes Management System** built using **Django (REST Framework)** and **React (Vite)** with **JWT authentication**, **PostgreSQL database**, **unit testing**, and **CI/CD using GitHub Actions**. The backend is deployed on **Railway**, and the frontend is deployed on **Vercel**.

---

## 🚀 Features

- 🔐 User Authentication (Register/Login/Logout) using JWT
- 📝 Create, Read , Delete Notes
- 📦 PostgreSQL as production-ready database
- ✅ Unit testing using Django `APITestCase`
- 📊 Code coverage with `coverage.py` and Codecov
- 🔁 CI/CD pipeline using GitHub Actions
- ☁️ Deployment using Railway (API) and Vercel (Frontend)
- 🌐 Secure CORS-enabled communication between frontend and backend

---

## ⚙️ Tech Stack

| Layer     | Technology               |
|-----------|--------------------------|
| Frontend  | React + Axios + Vite     |
| Backend   | Django + DRF             |
| Database  | PostgreSQL (via Railway) |
| Auth      | JWT (SimpleJWT)          |
| CI/CD     | GitHub Actions           |
| Hosting   | Railway (Backend API), Vercel (Frontend)
| Testing   | Django REST Framework `APITestCase`, `coverage.py`

---

## 🔧 Local Setup Instructions

### Backend (Django)

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
