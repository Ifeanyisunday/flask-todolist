from flask_login import current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, session, flash, request
from initialize_db import User, database

class UserService:
    def register_user(self, username, email, password):
        user = User(username, email, password)
        database.session.add(user)
        database.session.commit()
        return "User Registered"

    # def login_user(self, email, password):
    #     user = User.query.filter_by(email=email, password=password).first()
    #     if user and user.password == password:
    #         login_user(user)
    #         flash("Logged in successfully", "success")
    #         return render_template("taskdashboard.html")
    #     else:
    #         return "Wrong username or password"

    def logout_user(self):
            logout_user()
            return redirect(url_for('home'))
    def get_userid(self, user_id):
        return User.query.get(int(user_id))


class TaskService:
    def create_task(self, task):
        database.session.add(task)
        database.session.commit()
        return "Task Created"
