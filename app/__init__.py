from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    PrometheusMetrics(app)

    with app.app_context():
        db.create_all()

    return app
