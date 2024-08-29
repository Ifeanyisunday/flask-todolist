from flask_sqlalchemy import SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'mysql://root:vitalspring10@127.0.0.1/todoapp'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}"


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, description, done, user_id):
        self.title = title
        self.description = description
        self.done = done
        self.user_id = user_id
    def __repr__(self):
        return f"Task {self.title}", f"Done: {self.done}"