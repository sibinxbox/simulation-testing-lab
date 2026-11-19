import os
from flask import Blueprint, jsonify, render_template, request
from sqlalchemy import text
from app import db
from app.models import User

bp = Blueprint("main", __name__)

@bp.get("/")
def index():
    return render_template(
        "index.html",
        version=os.getenv("APP_VERSION", "0.1.0"),
        environment=os.getenv("APP_ENV", "development"),
    )

@bp.get("/health")
def health():
    return jsonify({"status": "healthy", "service": "simulation-testing-lab"})

@bp.get("/ready")
def ready():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "ready", "database": "ok"})
    except Exception as exc:
        return jsonify({"status": "not_ready", "database": "unavailable",
                        "error": str(exc)}), 503

@bp.get("/version")
def version():
    return jsonify({
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("APP_ENV", "development"),
    })

@bp.get("/api/info")
def info():
    return jsonify({
        "service": "simulation-testing-lab",
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("APP_ENV", "development"),
    })

@bp.get("/api/users")
def list_users():
    users = db.session.execute(db.select(User)).scalars().all()
    return jsonify([user.to_dict() for user in users])

@bp.post("/api/users")
def create_user():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    email = data.get("email", "").strip()

    if not username or not email:
        return jsonify({"error": "username and email are required"}), 400

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@bp.get("/api/status")
def status():
    return jsonify({"status": "running", "service": "simulation-testing-lab"})
