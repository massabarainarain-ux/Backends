# Masab Edit - Python & PostgreSQL Backend

This is the complete backend source code for **Masab Edit** using Python, Django, and PostgreSQL.

## 🚀 Setup Instructions

### 1. Prerequisite
Ensure you have Python 3.10+ and PostgreSQL installed on your machine.

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create PostgreSQL Database
Login to your PostgreSQL server and create a database named `masab_edit_db`:
```sql
CREATE DATABASE masab_edit_db;
```

### 5. Update Database Credentials
Open `masab_edit/settings.py` and modify the `DATABASES` dictionary with your local PostgreSQL user and password.

### 6. Run Migrations
```bash
python manage.py makemigrations api
python manage.py migrate
```

### 7. Create Superuser (Admin Dashboard Access)
```bash
python manage.py createsuperuser
```

### 8. Run Server
```bash
python manage.py runserver
```

The Django server will start at `http://127.0.0.1:8000/` and is fully connected to your dynamic React frontend! Any change you make in the Admin Dashboard will save permanently in PostgreSQL and update instantly across all users' devices.
