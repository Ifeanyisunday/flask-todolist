from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

database = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:vitalspring10@127.0.0.1/todoapp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)

    with app.app_context():
        database.create_all()

    return app


class User(UserMixin, database.Model):
    password_hash = database.Column(database.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    __table_name__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(80), nullable=False)
    tasks = database.relationship('Task', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}"



class Task(database.Model):
    __table_name__ = 'tasks'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(80), unique=True, nullable=False)
    description = database.Column(database.Text, nullable=False)
    done = database.Column(database.Boolean, default=False)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, description, done, user_id):
        self.title = title
        self.description = description
        self.done = done
        self.user_id = user_id

    def __repr__(self):
        return f"Task {self.title}", f"Done: {self.done}"
