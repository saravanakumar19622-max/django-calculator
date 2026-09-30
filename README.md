# Django Calculator

A simple calculator web application built with Django. It supports arithmetic operations, stores calculation history, and provides a contact form and informational pages.

## Features

- Addition, subtraction, multiplication, and division
- Calculation history stored in SQLite during local development
- Contact form with server-side validation
- Django admin interface
- Responsive static styling
- Production-ready configuration using environment variables
- WhiteNoise for serving static files
- Gunicorn configuration for deployment

## Tech Stack

- Python
- Django 5
- SQLite
- HTML/CSS
- Gunicorn
- WhiteNoise

## Run locally

```bash
python -m venv venv
```

Windows:
```bash
venv\\Scripts\\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a local environment file from `.env.example` and set a development secret if desired.

Run migrations:
```bash
python manage.py migrate
```

Start the server:
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## GitHub

Do not commit `.env`, `db.sqlite3`, `venv/`, `__pycache__/`, or production secrets. The included `.gitignore` handles these files.

## Deployment

The included `render.yaml` can be used with Render. Connect the GitHub repository, and Render will install dependencies, run migrations, collect static files, and start Gunicorn.

> Note: SQLite is suitable for a small demo/portfolio deployment. For a production multi-user application, use PostgreSQL or another persistent database.
