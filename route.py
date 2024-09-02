from flask import Flask, render_template, request, redirect, url_for, Config, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy.sql.functions import user

from services.user_service import UserService
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from initialize_db import database, create_app, User, Task


app = create_app()
app.secret_key = 'my secret key'


userservice = UserService()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    userservice.get_user_id(user_id)


with app.app_context():
    database.create_all()

@app.route("/menu")
def menu():
    return render_template('index.html')

@app.route("/update_page")
def update_page():
    return render_template('update.html')


@app.route("/")
def home():
    if 'email' in session:
        return redirect(url_for('taskpage'))
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/taskpage")
@login_required
def taskpage():
    return render_template('taskdashboard.html')


@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('signup.html')
        else:
            userservice.register_user(username, email, password)
            session['email'] = email
            return render_template("taskdashboard.html", message=f"{username} you are registered")
    else:
        flash("User already registered", "success")
        return render_template('index.html')


@app.route("/user_login", methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email, password=password).first()
        if user and user.password == password:
            login_user(user)
            session['email'] = email
            flash("Logged in successfully", "success")
            return render_template('taskdashboard.html', message=f"{user.username} you are logged in")
        else:
            return render_template('signup.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    userservice.logout_user()
    return render_template('index.html')


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    tasks = Task.query.all()

@app.route('/addtasks', methods=['POST'])
def addtasks():
    if "email" in session:
        user = User.query.filter_by(email=session['email']).first()
        if user:
            if request.method == 'POST':
                title = request.form.get('title')
                description = request.form.get('description')
                task1 = Task(title=title, description=description, user_id=user.id)
                task = Task.query.filter_by(title=title).first()
                if task:
                    return render_template('taskdashboard.html', message=f"{user.username} you added this Task already")
                else:
                    database.session.add(task1)
                    database.session.commit()
                    return render_template('taskdashboard.html', message=f"{user.username} you just added {title} as new task")


@app.route('/updatetasks', methods=['POST'])
def updatetasks():
    if "email" in session:
        user = User.query.filter_by(email=session['email']).first()
        if user:
            if request.method == 'POST':
                previous_title = request.form.get('previous_title')
                task = Task.query.filter_by(title=previous_title).first()
                if task:
                    title = request.form.get('title')
                    description = request.form.get('description')
                    task = Task(title=title, description=description, user_id=user.id)
                    database.session.commit()
                    return render_template('update.html', message=f"{user.username} you just updated to {title} as new task")


@app.route('/tasks/<int:task_id>', methods=['GET', 'POST'])
def task_done(task_id):
    task = Task.query.filter_by(id=task_id).first()
    done = request.form.get('done')
    user = User.query.filter_by(id=task.user_id).first()
    if done:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form.get('request_title')
        description = request.form.get('request_description')

if __name__ == "__main__":
    app.run(debug=True)
