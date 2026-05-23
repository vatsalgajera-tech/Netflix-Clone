# 🎬 Netflix Clone

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
</p>

<p align="center">
  A full-stack Netflix Clone web application built with Python and Django for streaming movies and TV shows, featuring custom admin dashboards, user profiles, and an interactive UI.
</p>

---

## 📌 Overview

The **Netflix Clone** is a dynamic, fully responsive web application that replicates the core functionality and design of the popular streaming platform Netflix. It includes a user-facing frontend for browsing and watching content, alongside a powerful custom admin dashboard for content and user management.

This project demonstrates practical experience with:

- Full-Stack Django Development
- User Authentication & Authorization
- Dynamic Database Management (SQLite)
- Media File Handling
- Custom Admin Dashboards
- Responsive Frontend UI Design

---

## ✨ Features

### 👨💼 Admin Dashboard Module
- Secure Custom Admin Login
- Manage Users and Profiles
- Add, Update, and Delete Movies and TV Series
- Manage Categories and Genres
- Upload Video Files and Posters
- Monitor Total Content Analytics

### 👨🎓 User Module
- User Registration, Login, and Password Management
- Browse Movies and TV Series
- Search for Specific Content
- Add/Remove Content to "My List"
- Watch Videos in an Integrated Player
- Manage User Profiles

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,django,sqlite,html,css,js,git,github,vscode" />
</p>

---

## 📂 Project Structure

```text
Netflix-Clone/
├── core/                  # Core app for movies, series, and main views
├── dashboard/             # Custom admin dashboard app
├── media/                 # Uploaded media (video files, posters)
├── netflix_clone/         # Main project configuration folder
├── static/                # Static files (CSS, JS, Images)
├── templates/             # HTML templates (core, dashboard, account)
├── users/                 # Custom user and profile management app
├── db.sqlite3             # SQLite Database
├── manage.py              # Django management script
├── populate_db.py         # Script to seed demo data
└── README.md
```

---

## 🗄️ Core Modules

- Authentication & Account Management
- Profile Management
- Content Streaming (Video Player)
- My List (Watchlist functionality)
- Search & Filtering functionality
- Custom Content Management System (CMS)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vatsalgajera-tech/Netflix-Clone.git
cd Netflix-Clone
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

- **Windows:**
```bash
venv\Scripts\activate
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

*(If you have a `requirements.txt` file)*
```bash
pip install -r requirements.txt
```
*(Otherwise, install Django manually)*
```bash
pip install django
```

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7️⃣ Seed Demo Data (Optional)

```bash
python populate_db.py
```

### 8️⃣ Run Backend Server

```bash
python manage.py runserver
```

### 9️⃣ Open in Browser

```text
http://127.0.0.1:8000
```

---

## 🔐 User Roles

| Role | Access |
|------|--------|
| Superuser (Admin) | Full access to Django admin and custom dashboard to manage all users, movies, series, and categories |
| User | Can create multiple profiles, browse content, watch videos, and manage their personal "My List" |

---

## 🚀 Future Enhancements

- Subscription and Payment Integration (Stripe)
- Advanced Recommendation Algorithm
- Email Verification and Reset Password via Email
- Continue Watching Feature
- Deployment to Production (AWS / Heroku / Vercel)

---

## 🧠 Key Learnings

Through this project, I gained hands-on experience with:

- Django ORM and Database Modeling
- Handling Custom User Models in Django
- Creating Custom Admin Interfaces without relying solely on Django's default admin
- Working with Static and Media files in Django
- Building scalable Full-Stack applications

---

## 👨💻 Author

### Vatsal Gajera

- GitHub: https://github.com/vatsalgajera-tech
- LinkedIn: https://www.linkedin.com/in/vatsalgajera/
- Email: vatsalgajera.tech@gmail.com

---

## ⭐ Show Your Support

If you found this project useful, please give it a ⭐ on GitHub.

---

## 📜 License

This project is developed for educational and portfolio purposes.
