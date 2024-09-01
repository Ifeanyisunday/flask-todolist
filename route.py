from flask import Flask, render_template, request, redirect, url_for, Config, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from services.user_service import UserService, TaskService
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from initialize_db import database, create_app, User, Task


app = create_app()
app.secret_key = 'my secret key'


userservice = UserService()
taskservice = TaskService()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from services.user_service import UserService
    UserService.get_userid(user_id)


with app.app_context():
    database.create_all()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/task_page")
@login_required
def task_page():
    return render_template('taskdashboard.html')


@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        userservice.register_user(username, email, password)
    else:
        flash("User already registered", "success")
        return render_template('signup.html')


@app.route("/user_login", methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email, password=password).first()
        if user and user.password == password:
            login_user(user)
            flash("Logged in successfully", "success")
            return render_template("taskdashboard.html")
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    userservice.logout_user()
    return redirect(url_for('login'))

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    tasks = Task.query.all()


@app.route('/tasks/<int:task_id>', methods=['GET', 'POST'])
def task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        done = request.form.get('done')
        user = User.query.filter_by(id=task.user_id).first()
        if done:
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('index'))


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
