# Django Blog Project

## 📄 Introduction
A fully functional **Blog Application built with Django**, allowing users to create, view, and manage blog posts. This project demonstrates how to use Django to build a blog with user authentication, search functionality, and responsive design.
## Table of Contents
- [Introduction](#-introduction)
- [Features](#-features)
- [Technologies](#-technologies)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Conclusion](#-conclusion)
- [Get Started](#-get-started)
## ✨ Features
- User authentication (login, register, logout)
- Create, update, and delete blog posts
- View all blogs and search for specific blogs
- Responsive design using Bootstrap 5
- Search functionality that logs all search queries
- File logging for search queries
- Comment section (optional)
## 🛠️ Technologies
- **Django**: Backend framework for building web applications
- **Bootstrap 5**: Frontend framework for responsive design
- **SQLite**: Database for storing blog posts and user data
- **HTML, CSS**: For styling the front end
- **JavaScript**: For adding interactive elements
## 🏗️ Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/AritriPodde2210/django-blog-project.git
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
4.Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run migrations:
    ```bash
    python manage.py migrate
    ```
6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```
## 🧑‍💻 Usage
1. Open your browser and go to `http://127.0.0.1:8000/`
2. Register an account or login to create, view, and manage your blog posts.
3. Search for blogs using the search bar.
4. Logged search queries will be stored in a log file.
## 🗂️ Project Structure
```plaintext
django-blog-project/
│
├── blog_project/             # Main Django project directory
│   ├── blog/                 # Blog application directory
│   ├── blog_project/         # Project settings and configuration
│   ├── templates/            # HTML templates for frontend
│   ├── static/               # Static files (CSS, JavaScript)
│   ├── media/                # Uploaded files (images, etc.)
│   └── manage.py             # Django management script
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## 🖼️ Screenshots
Here are a few snapshots showcasing the main features of the Django Blog Project:
### 🏠 Home Page and Blog_details Page
Displays the list of recent blog posts and a search bar at the top for searching blog content.
![Home Page](![Home](https://github.com/user-attachments/assets/6dcfca93-7aa6-4319-af4e-f7fbf0e72211)
)
### 🔑 Login Page
User authentication form for logging into the system.

![Login Page](![Login](https://github.com/user-attachments/assets/3a9faccf-ee0a-45f5-a341-5c6c385d41d4)
)
### 📝 Blog Create Page
Detailed view of a single blog post with the option to edit or delete the post (if logged in as the author).

![Blog Details](![Create_Blog](https://github.com/user-attachments/assets/7ebc8259-6871-454f-acdb-7e86e65ba688)
)
### 🔍 Search Results Page
Search results displaying relevant blog posts based on user queries.

![Search Results])(![Search_Results](https://github.com/user-attachments/assets/bc54659c-244d-4739-bb0e-40d4d3817f63))

## 🚀 Conclusion
This Django Blog Project demonstrates how to build a scalable and responsive blog application using Django and Bootstrap. It includes essential features such as user authentication, blog management, and a fully responsive design.



