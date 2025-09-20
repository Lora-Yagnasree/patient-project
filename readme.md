# Patient Management API

A Django REST Framework (DRF) project that manages patients, dropdown options, and authentication (register/login with JWT).
Includes role-based access for admin/staff and normal users.

# Features

## Authentication
- User registration with email & password
- JWT-based login (access & refresh tokens)
- Role-based access (Admin/User)

## Patient Management
- Add, update, delete, and view patient records
- Normal users only see their own patients
- Admins can view all patients

## Dropdown Management
- Admin can add dropdown values (blood group, relation, etc.)
- Users can fetch dropdown values grouped by field name

## Validation
- Mobile number (10 digits, starts with 6–9)
- Pin code (6 digits)
- Date of birth (cannot be in future)

# Tech Stack

- Backend: Django 5, Django REST Framework

- Auth: JWT (via djangorestframework-simplejwt)

- Database: SQLite (default, can use PostgreSQL/MySQL)

- Python: 3.10+
**Project Structure**
    ```bash
        app3monkeys/
        ├── models.py
        ├── serializers.py
        ├── views.py
        ├── urls.py
        ├── permissions.py
        careerportal/
        ├── settings.py
        ├── urls.py

# Authentication Flow

- Register User → /api/register/

- Login with Email/Password → /api/login/

- Receive JWT tokens (access + refresh)

- Use Authorization: Bearer <access_token> for protected APIs
# Installation & Setup

**1. Clone the repo**
    ```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
**2. Create virtual environment**
    ```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

**3. Install dependencies**
    ```bash
pip install -r requirements.txt

**4. Run migrations**
    ```bash
python manage.py migrate

**5. Create superuser**
    ```bash
python manage.py createsuperuser

**6. Run server**
    ```bash
    python manage.py runserver ```

# API Endpoints

- register API
- login API
- patients API
- dropdownoptions API 

# Roles

- Admin/Staff

  - Full access to all patients

   - Can manage dropdown options

- Normal User

   - Can only see their submitted patients 

#  Dependencies

Add this to your requirements.txt:

Django>=5.0
djangorestframework
djangorestframework-simplejwt

