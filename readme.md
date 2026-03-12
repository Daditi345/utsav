# FastAPI Application Setup Guide

This project is a FastAPI application.

---

## 📦 1. Create a Virtual Environment

Create a virtual environment using:

```bash
python -m venv venv
```

---

## ▶️ 2. Activate the Virtual Environment

### Windows:
```bash
venv\Scripts\activate
```

### macOS / Linux:
```bash
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal.

---

## 📥 3. Install Dependencies

`pip` is the Python package manager.

To install all required dependencies from `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

---

## 🧠 4. Select Python Interpreter in VS Code

In VS Code:

1. Press: `Ctrl + Shift + P`
2. Search for: `Python: Select Interpreter`
3. Choose the interpreter from your virtual environment (`venv`).

---

## 🚀 5. Run the FastAPI Application

Start the application using:

```bash
uvicorn main:app --reload
```

- `main` → Python file name  
- `app` → FastAPI instance  

The application will run at:

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation:

Swagger UI:
```
http://127.0.0.1:8000/docs
```

ReDoc:
```
http://127.0.0.1:8000/redoc
```

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- Uvicorn
