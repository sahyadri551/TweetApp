# TweetApp

A social media application TweetApp built with Django, Tailwind CSS, and Alpine.js.
Users can create posts with images, interact through likes and comments, follow other users, and browse personalized feeds.

## Features
### Authentication
* User Registration
* User Login
* User Logout
* Django Authentication System

### User Profiles
* Public User Profiles
* Profile Editing
* Avatar Upload
* Bio & Personal Information
* User Statistics
  * Tweets Count
  * Followers Count
  * Following Count

### Tweets
* Create Tweet
* Edit Tweet
* Delete Tweet
* Image Upload Support
* Responsive Tweet Feed

### Comments
* Add Comments
* Edit Comments
* Delete Comments
* Comment Counts

### Likes
* Like Tweets
* Unlike Tweets
* Live Like Counts

### Follow System
* Follow Users
* Unfollow Users
* Followers Page
* Following Page

### Feed System
* Following Feed
* Explore Feed
* Personalized Timeline

## Tech Stack
### Backend
* Python
* Django

### Frontend
* HTML
* Tailwind CSS
* Alpine.js

### Database
* SQLite (Development)
* PostgreSQL

### Authentication
* Django Authentication Framework

## Project Structure
TweetApp/
│
├── Tweet/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── media/
├── static/
├── templates/
│
├── manage.py
└── requirements.txt

## Installation

### Clone Repository
git clone https://github.com/<your-username>/TweetApp.git
cd TweetApp

### Create Virtual Environment
```python -m venv .venv```
### Activate Virtual Environment
```.venv\Scripts\activate```

### Install Dependencies
``` pip install -r requirements.txt ```

### Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser
```python manage.py createsuperuser```

### Run Development Server
```python manage.py runserver```

Open:
```http://127.0.0.1:8000/```

## Environment Variables
Create a `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

## Future Improvements

* Search Users
* Notifications
* Infinite Scrolling
* Hashtags
* Bookmark Tweets
* Direct Messaging
* REST API
* Docker Support
* 
## Learning Outcomes
This project was built to learn and practice:
* Django Models
* Django Views
* Django Templates
* Authentication & Authorization
* CRUD Operations
* Model Relationships
* File Upload Handling
* Tailwind CSS Integration
* Alpine.js Interactivity
* User-to-User Relationships
* Feed Personalization

---

## Author

**Sahyadri Manglam**

Built as a hands-on Django learning project focused on understanding full-stack web development concepts and social media application architecture.
