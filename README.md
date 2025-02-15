# JustiFy

JustiFy is a Django-powered web application designed for crime reporting and community verification. Built for the NSU WebXtreme Hackathon 2025 and developed entirely by me, JustiFy enables verified users to report crimes by uploading images (mandatory) or videos (optional), and leverages AI to generate descriptions for image-based reports. The platform also supports secure authentication, community voting, and real-time filtering and searching of crime posts.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

JustiFy empowers communities to take action by providing a secure platform where users can report crimes with multimedia evidence. Key functionalities include:
- **Secure User Authentication:** Registration, login, password management, OTP phone verification, and JWT-based authorization.
- **Crime Reporting:** Verified users can submit crime reports with mandatory images and optional videos. AI tools generate descriptions for image-based reports, while video uploads require manual descriptions.
- **Community Verification:** Users can upvote/downvote posts, comment (with proof attachments), and interact with the crime feed, which supports filtering, sorting, and searching.
- **User Profiles:** Each user has a profile displaying their details and submitted crime reports.

## Features

- **User Authentication & Authorization**
  - Registration with email, password, and phone number.
  - OTP-based phone verification.
  - JWT authentication and refresh tokens.
  - Password management and recovery.
  - Admin controls for banning users.

- **Crime Reporting**
  - Verified users can report crimes with image uploads (mandatory) and optional video.
  - Auto-generation of crime descriptions via AI for image-based posts.
  - Location selection using divisions and districts of Bangladesh.

- **Community Interaction**
  - Upvote/downvote crime reports.
  - Commenting with mandatory proof attachments.
  - Crime posts assigned a verification score based on community feedback.

- **Crime Feed**
  - Paginated display of crime posts.
  - Filtering by location and verification score.
  - Sorting by date and community engagement.
  - Keyword search for posts.

- **Responsive Design & Security**
  - Mobile-friendly interface.
  - Secure coding practices (password hashing, protection against SQL injection, XSS, and CSRF).

## Tech Stack

- **Backend:** Django, Python
- **Frontend:** Django Templates (or integrated React if desired)
- **Database:** SQLite/PostgreSQL/MySQL (configurable)
- **Authentication:** JWT, OTP-based verification
- **AI Integration:** OpenAI GPT or similar tool for generating descriptions from images
- **APIs:** Integration with APIs (or static lists) for Bangladeshi divisions and districts

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/duttaturja/JustiFy.git
   cd JustiFy
   ```
   
2. **Create a Virtual Environment**
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

   ```
   
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
   
4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a Superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**

   Production: http://127.0.0.1:8000/

## Usage
**1. User Registration & OTP Verification**

  - Register a new user at /users/register/.
  - Upon registration, a random OTP is generated and displayed.
  - Verify your phone number by entering the OTP .
  
**2. Reporting a Crime**

  - Log in and navigate to /reports/create/ to submit a crime report.
  - Upload an image (mandatory) or video (optional). For image-only submissions, a dummy AI-generated description is auto-filled.

**3. Community Interaction**

  - Browse crime reports on the feed at /reports/feed/ (or the home page).
  - Click on any report to view details, vote (upvote/downvote), and add comments with proof attachments.
    
**4. Filtering & Sorting the Feed**

  - Filter reports by adding URL query parameters (e.g., ?division=Dhaka&district=Dhaka).
  - Sort the feed by upvotes .

## Project Structure

```plaintext
JustiFy/
├── JustiFy/             # Main application directory
│   ├── __init__.py
│   ├── asgi.py          # ASGI application
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL configurations
│   └── wsgi.py          # WSGI application
├── crime/               # Crime application directory
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── user/                # User application directory
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/              # Static files (CSS, images, JavaScript)
│   ├── css/
│   ├── images/
│   └── js/
├── templates/           # HTML templates
│   ├── base.html
│   ├── errors/          # Error templates
│   ├── user/            # User app templates
│   └── crime/           # Crime app templates
├── .gitignore           # Git ignore file
├── db.sqlite3           # SQLite database file
├── manage.py            # Django management script
└── requirements.txt    # Python dependencies
```

Contributing
I am developing JustiFy as a solo project, but contributions are welcome! If you find bugs or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the Apache License 2.0.

Contact
Developer: Turja Dutta
GitHub: duttaturja
Email: duttaturja@gmail.com
