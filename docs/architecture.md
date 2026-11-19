# Architecture

Nginx is the public reverse proxy. Flask/Gunicorn is the application layer. PostgreSQL stores persistent data.

Request path:
Browser -> Nginx:8080 -> app:5000 -> PostgreSQL:5432
