# Healthcare Backend - Django Assignment

**Submitted By:**  
Name: Aadish Garg

Enrollment Number: E23CSEU0611 

Email: e23cseu0611@bennett.edu.in 

Personal Email: aadishgarg15@gmail.com

---

## Project Overview

This project is a Healthcare Backend System built using:

- Django
- Django REST Framework (DRF)
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)

The system allows users to register, log in securely using JWT authentication, and manage patient and doctor records. It also supports assigning doctors to patients through a mapping system.

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT (SimpleJWT)
- python-dotenv

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd healthcare_backend
```

### 2️⃣ Create Virtual Environment

``` bash
python -m venv venv
venv\Scripts\activate   # On Windows
```


### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a .env file in the root directory using .env.example as reference.

#### Example:

```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Server will start at:
```bash 
http://127.0.0.1:8000/
```

### Important commands

| Method | Endpoint            | Description                 |
| ------ | ------------------- | --------------------------- |
| POST   | /api/auth/register/ | Register a new user         |
| POST   | /api/auth/login/    | Login and receive JWT token |


| Method | Endpoint            | Description                                    |
| ------ | ------------------- | ---------------------------------------------- |
| POST   | /api/patients/      | Create new patient                             |
| GET    | /api/patients/      | Get all patients created by authenticated user |
| GET    | /api/patients/<id>/ | Get specific patient details                   |
| PUT    | /api/patients/<id>/ | Update patient                                 |
| DELETE | /api/patients/<id>/ | Delete patient                                 |


| Method | Endpoint            | Description                                    |
| ------ | ------------------- | ---------------------------------------------- |
| POST   | /api/patients/      | Create new patient                             |
| GET    | /api/patients/      | Get all patients created by authenticated user |
| GET    | /api/patients/<id>/ | Get specific patient details                   |
| PUT    | /api/patients/<id>/ | Update patient                                 |
| DELETE | /api/patients/<id>/ | Delete patient                                 |


| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| POST   | /api/doctors/      | Create new doctor   |
| GET    | /api/doctors/      | Get all doctors     |
| GET    | /api/doctors/<id>/ | Get specific doctor |
| PUT    | /api/doctors/<id>/ | Update doctor       |
| DELETE | /api/doctors/<id>/ | Delete doctor       |


### Security Features

JWT-based Authentication
Protected Endpoints using IsAuthenticated
PostgreSQL database integration
Environment variables for sensitive configurations
Proper validation and error handling

### Expected Functionality

Users can register and log in securely.
Authenticated users can manage patients and doctors.
Doctors can be assigned to patients.
All data is stored securely in PostgreSQL.
All endpoints are tested using Postman.
