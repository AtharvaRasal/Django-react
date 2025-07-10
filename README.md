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
```

🗝️ Create a .env file in the root of the backend/ directory with:

```bash
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```
Use Railway to provision the database and copy credentials from its dashboard.

---

### Frontend (React)

```bash
cd frontend
npm install
npm run dev
```
🗝️ Create a .env file in frontend/ directory:

```bash
VITE_API_URL=https://your-backend-url.up.railway.app
```
This will connect the frontend to your live backend API.

---

🧪 Testing

Unit tests for backend API are located in backend/api/tests.py.

🗝️ To run tests:

```bash
coverage run manage.py test
coverage report
coverage html
```

✅ Test Coverage Badge
CI/CD automatically uploads coverage to Codecov

---

🔄 CI/CD with GitHub Actions:

✅ Auto install & test backend on every commit.

📤 Upload coverage report to Codecov.

🚀 Deploy backend to Railway and frontend to Vercel automatically on push to main.

---

📁 Project Structure:

```bash
django-react/
│
├── backend/            # Django project (API)
│   ├── api/            # Notes app
│   ├── tests.py        # Unit tests
│   ├── requirements.txt
│   ├── start.sh
│   └── ...
│
├── frontend/           # React app
│   ├── src/
│   ├── public/
│   ├── .env
│   └── ...
│
├── .github/workflows/  # GitHub Actions config
│
├── README.md
└── ...
```

---

🌍 Live Demo:https://django-react-kappa.vercel.app/login

---

📸 Screenshots:

# Register

<img width="1356" height="667" alt="Screenshot 2025-07-10 203214" src="https://github.com/user-attachments/assets/857d46d9-dd4d-4321-9865-009cdaefff0b" />

# Login

<img width="1365" height="650" alt="Screenshot 2025-07-10 203239" src="https://github.com/user-attachments/assets/59573ad7-67f3-45c4-8959-671adb5fa735" />

# Notes

<img width="1357" height="679" alt="Screenshot 2025-07-10 203106" src="https://github.com/user-attachments/assets/8d69609e-3200-4e24-8fbc-18af7f9fd6f2" />
