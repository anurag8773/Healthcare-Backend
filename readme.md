# Healthcare Backend API

A **Healthcare Backend System** built with **Django, Django REST Framework, PostgreSQL, and JWT Authentication**.

It provides a secure RESTful API to manage **patients, doctors, and their mappings** (assignments), with authentication and authorization for protected resources.

---

## Features

 **User Authentication & Authorization**

* Register new users with email & password
* JWT-based authentication (`djangorestframework-simplejwt`)

 **Patient Management**

* Create, update, delete, and retrieve patient records
* Patients are linked to the authenticated user who created them

 **Doctor Management**

* Create, update, delete, and retrieve doctor records

 **Patient-Doctor Mapping**

* Assign doctors to patients
* Retrieve all doctors for a specific patient
* Remove doctor-patient mapping

 **Secure APIs**

* Protected endpoints require a JWT `access` token
* Permissions restrict unauthorized access

 **PostgreSQL Database**

* Uses Django ORM with PostgreSQL for reliable storage

 **Dockerized Setup**

* Easily run the application with **Docker + docker-compose**

---

## Project Structure

```
healthcare_backend/
│── apps/
│   ├── users/          # Custom user model & auth endpoints
│   ├── patients/       # Patient CRUD API
│   ├── doctors/        # Doctor CRUD API
│   └── mappings/       # Patient-Doctor assignment
│
│── healthcare_backend/
│   ├── settings.py     # Django settings
│   ├── urls.py         # Global URL routing
│   └── wsgi.py         # WSGI entry point
│
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── manage.py
└── README.md
```

---

##  Tech Stack

* **Backend Framework:** Django 5.x + Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** JWT (`djangorestframework-simplejwt`)
* **Containerization:** Docker + docker-compose
* **API Testing:** Postman

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anurag8773/Healthcare-Backend.git
cd Healthcare-Backend
```

---

### 2. Setup Environment Variables

Create a `.env` file with the following values:

```
DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=healthcare_db
POSTGRES_USER=healthcare_user
POSTGRES_PASSWORD=securepassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

### 3. Run with Docker

Make sure you have **Docker & docker-compose installed**.

Then start the app:

```bash
docker-compose up --build -d
```

This will:
 Start PostgreSQL
 Start Django app at `http://localhost:8000`

---

### 4. Run Migrations

```bash
docker-compose exec web python manage.py migrate
```

---

### 5. Create Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

Then log in to the **Admin Panel** at:

```
http://localhost:8000/admin/
```

---

## Postman Collection

You can easily test all APIs using the provided Postman collection.

- **[Postman Collection](https://documenter.getpostman.com/view/37271849/2sB34oBHEt)**  
- **Base URL:** `http://localhost:8000/api/`

**Steps to use:**
1. Download the collection JSON file.
2. Import it into Postman (File → Import).
3. Set the base URL as `http://localhost:8000`.
4. First run `Auth → Register` and `Auth → Login` to get JWT token.
5. Use the token for all secured APIs.

---

##  Example API Flow

1️⃣ **Register** user → `/auth/register/`.
2️⃣ **Login** → `/auth/login/` → get JWT token.
3️⃣ **Create Patients & Doctors**.
4️⃣ **Assign Doctor to Patient** → `/mappings/`.
5️⃣ **Retrieve All Doctors for a Patient** → `/mappings/{patient_id}/`.

---

## Authentication

Uses **JWT (JSON Web Token)**.

* Get token via `POST /auth/login/`
* Use token in headers:

```
Authorization: Bearer <your_access_token>
```

---

## Assumptions

* Users are **healthcare staff/admins** managing patients & doctors
* Patients belong to the **authenticated user who created them**
* Doctors are globally available for all users
* A patient can have **multiple doctors assigned**
* Minimal patient & doctor details (can be extended later)

---

## Future Scope

*  Role-based access control (e.g. Admin, Doctor, Staff)
*  Appointment scheduling
*  Medical history & prescriptions
*  Pagination & filtering for large datasets

---

## Quick Docker Commands

* **Start Services:**

  ```bash
  docker-compose up -d
  ```
* **View Logs:**

  ```bash
  docker-compose logs -f web
  ```
* **Run Migrations:**

  ```bash
  docker-compose exec web python manage.py migrate
  ```
* **Create Superuser:**

  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```
* **Stop Services:**

  ```bash
  docker-compose down
  ```
---

##  Author  

**Anurag Kumar Maurya**   

  
