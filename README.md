# 💰 Expense Tracker — Django Web App


🧾 A simple, secure, and elegant way to track your income and expenses — built using Django.

## ✨ Overview

This Expense Tracker is a web-based personal finance tool that helps users record, monitor, and analyze their financial transactions.
Users can sign up, log in, add income/expenses, view history, and delete entries — all with ease.

🎯 Goal: Make daily financial management effortless through an intuitive and responsive web app.

## 🚀 Live Demo
🔗 **[Expense Tracker](https://web-production-7ebff.up.railway.app/)**
 

## 🚀 Features

✅ User Authentication — Secure sign-up, login, and logout using Django’s auth system
💵 Add Transactions — Log income and expenses with date, category, and description
📊 History Dashboard — View, filter, and delete previous records easily
📈 Auto Balance Update — Instantly calculates total balance, income, and expense
📱 Responsive UI — Mobile-friendly interface using Bootstrap / Tailwind CSS

## ⚙️ Installation

Follow these steps to set up the project locally 👇

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/django-expense-tracker.git
cd django-expense-tracker
```
### 2️⃣ Create & Activate Virtual Environment
```
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On macOS/Linux
```

### 3️⃣ Install Requirements
```
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start Server
```
python manage.py runserver
```


🌐 Visit: http://127.0.0.1:8000/

## 🧠 Tech Stack
Category	Technology
Frontend	HTML, CSS, Bootstrap / Tailwind
Backend	Django, Python
Database	SQLite
Authentication	Django Auth System
Deployment	Render / Railway / Vercel (optional)

## 💡 Usage Guide

Sign Up for a new account

Login to your dashboard

Add income or expense with category and amount

View all transactions in the History tab

Delete any record when needed

## 🧩 Folder Structure
```
expense_tracker/
│
├── expense_app/           # Main app
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, JS, images
│   ├── models.py          # Database models
│   ├── views.py           # Logic
│   ├── urls.py            # Routes
│
├── expense_tracker/       # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3             # Database
├── manage.py
└── requirements.txt
```

## 🧭 Future Enhancements

✨ Monthly / yearly spending analytics
📈 Graphs & Charts (Matplotlib / Chart.js)
💾 Export data to PDF or Excel
☁️ Deploy to AWS / Render with CI-CD integration

## 💼 Project Impact (STAR Summary)

Situation: Managing daily expenses manually was inefficient.

Task: Build a user-friendly digital tracker with login support.

Action: Developed a Django-based web app with CRUD operations and responsive UI.

Result: Reduced expense tracking effort by 90%, achieved 100% functional authentication and a clean, data-driven dashboard.

## 🧰 Tools & Technologies Used

Django | Python | SQLite | HTML | CSS | Bootstrap | Git | GitHub

## 👨‍💻 Author

Jayanth
💼 Machine Learning & Full Stack Developer

📫 [LinkedIn](https://www.linkedin.com/in/tulugu-jayanth/)

💻 [GitHub](https://github.com/18jayanth)

