from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vitalspring10@127.0.0.1/todoapp'

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    return app