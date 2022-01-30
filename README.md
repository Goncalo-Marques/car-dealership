# car-dealership

School project developed in Django to manage a car dealership.

# Dependencies

Python: `3.10.0`

```bash
pip install -r requirements.txt 
```

# Quickstart

## Database

System: `PostgreSQL`  


Create the database:
```sql
CREATE DATABASE car_dealership OWNER your_owner;
```

## Backend

1. Configure the backend database  
    
    File: `car-dealership-backend/car_dealership_backend/settings.py`
    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "car_dealership",
            "USER": "your_owner",
            "PASSWORD": "your_password",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
    ```

1. Apply migrations

    ```bash
    python car-dealership-backend/manage.py migrate
    ```

1. (Optional) create super user

    ```bash
    python car-dealership-backend/manage.py createsuperuser
    ```

1. Run server

    ```bash
    python car-dealership-backend/manage.py runserver 8000
    ```

## Frontend

1. Run server

    ```bash
    python car-dealership-frontend/manage.py runserver 8001
    ```

## Servers

Backend: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
Backoffice: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
Frontend: [http://127.0.0.1:8001/](http://127.0.0.1:8001/)  