Here’s a **professional README.md** for your Healthcare Backend project ✅

---

# 🏥 Healthcare Backend API

A **Healthcare Backend System** built with **Django, Django REST Framework, PostgreSQL, and JWT Authentication**.

It provides a secure RESTful API to manage **patients, doctors, and their mappings** (assignments), with authentication and authorization for protected resources.

---

## 📌 Features

✅ **User Authentication & Authorization**

* Register new users with email & password
* JWT-based authentication (`djangorestframework-simplejwt`)

✅ **Patient Management**

* Create, update, delete, and retrieve patient records
* Patients are linked to the authenticated user who created them

✅ **Doctor Management**

* Create, update, delete, and retrieve doctor records

✅ **Patient-Doctor Mapping**

* Assign doctors to patients
* Retrieve all doctors for a specific patient
* Remove doctor-patient mapping

✅ **Secure APIs**

* Protected endpoints require a JWT `access` token
* Permissions restrict unauthorized access

✅ **PostgreSQL Database**

* Uses Django ORM with PostgreSQL for reliable storage

✅ **Dockerized Setup**

* Easily run the application with **Docker + docker-compose**

---

## 📂 Project Structure

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

## ⚙️ Tech Stack

* **Backend Framework:** Django 5.x + Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** JWT (`djangorestframework-simplejwt`)
* **Containerization:** Docker + docker-compose
* **API Testing:** Postman

---

## 🚀 Installation & Setup

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend
```

---

### ✅ 2. Setup Environment Variables

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

### ✅ 3. Run with Docker

Make sure you have **Docker & docker-compose installed**.

Then start the app:

```bash
docker-compose up --build -d
```

This will:
✅ Start PostgreSQL
✅ Start Django app at `http://localhost:8000`

---

### ✅ 4. Run Migrations

```bash
docker-compose exec web python manage.py migrate
```

---

### ✅ 5. Create Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

Then log in to the **Admin Panel** at:

```
http://localhost:8000/admin/
```

---

## 🧪 API Testing

### ✅ Base URL

```
http://localhost:8000/api/
```

---

### ✅ Auth APIs

* **Register** → `POST /api/auth/register/`
* **Login** → `POST /api/auth/login/` → returns JWT token

> Use `Authorization: Bearer <access_token>` for all other APIs.

---

### ✅ Patient APIs

* `POST /api/patients/` → Create patient
* `GET /api/patients/` → List patients for logged-in user
* `GET /api/patients/{id}/` → Get details of a patient
* `PUT /api/patients/{id}/` → Update patient
* `DELETE /api/patients/{id}/` → Delete patient

---

### ✅ Doctor APIs

* `POST /api/doctors/` → Create doctor
* `GET /api/doctors/` → List doctors
* `GET /api/doctors/{id}/` → Doctor details
* `PUT /api/doctors/{id}/` → Update doctor
* `DELETE /api/doctors/{id}/` → Delete doctor

---

### ✅ Mappings APIs

* `POST /api/mappings/` → Assign doctor to patient
* `GET /api/mappings/` → List all mappings
* `GET /api/mappings/{patient_id}/` → List all doctors assigned to a patient
* `DELETE /api/mappings/{mapping_id}/` → Remove a doctor-patient mapping

---

## ✅ Example API Flow

1️⃣ **Register** user → `/auth/register/`
2️⃣ **Login** → `/auth/login/` → get JWT token
3️⃣ **Create Patients & Doctors**
4️⃣ **Assign Doctor to Patient** → `/mappings/`
5️⃣ **Retrieve All Doctors for a Patient** → `/mappings/{patient_id}/`

---

## 🔐 Authentication

Uses **JWT (JSON Web Token)**.

* Get token via `POST /auth/login/`
* Use token in headers:

```
Authorization: Bearer <your_access_token>
```

---

## ✅ Admin Panel

Once superuser is created, access the admin panel at:

```
http://localhost:8000/admin/
```

Manage:
✅ Users
✅ Patients
✅ Doctors
✅ Patient-Doctor Mappings

---

## 📌 Assumptions

* Users are **healthcare staff/admins** managing patients & doctors
* Patients belong to the **authenticated user who created them**
* Doctors are globally available for all users
* A patient can have **multiple doctors assigned**
* Minimal patient & doctor details (can be extended later)

---

## 🔮 Future Scope

* ✅ Role-based access control (e.g. Admin, Doctor, Staff)
* ✅ Appointment scheduling
* ✅ Medical history & prescriptions
* ✅ Pagination & filtering for large datasets
* ✅ API versioning for backward compatibility
* ✅ Deploy to production with Gunicorn/Nginx

---

## 🐳 Quick Docker Commands

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

## 📝 License

MIT License © 2025

---

Would you like me to also:

✅ Generate a **sample Postman Collection JSON** with all APIs pre-configured?
✅ Or add **example request/response JSON** for each endpoint inside this README?
