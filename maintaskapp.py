from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from services.user import User_service

app = Flask(__name__)
Bootstrap(app)

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="vitalspring10",
    port='3306',
    database="todoapp"
)


# mydatabase = db.cursor()
# mydatabase.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, is_logged_in INT DEFAULT 0)")


@app.route("/")
def home():
    return render_template('signup.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_validation(username, password)

        try:
            if username and password:
                user_service = User_service()
                user_service.register_users(username, password)
                return render_template('taskdashboard.html')
        except Exception as message:
            message = str("User already exists")
            return f'Error: {message}'
    else:
        return render_template('signup.html')


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_validation(username, password)

        try:
            if username and password:
                user_service = User_service()
                user_service.register_users(username, password)
                return render_template('taskdashboard.html')
        except Exception as message:
            message = str("User already exists")
            return f'Error: {message}'
    else:
        return render_template('login.html')


def user_validation(username, password):
    if username == "" or password == "":
        return "Please fill all fields"
    elif username == "  " or password == "   ":
        return "Please fill all fields"

    # db = mysql.connector.connect(
    #     host="127.0.0.1",
    #     user="root",
    #     passwd="vitalspring10",
    #     port='3306',
    #     database="todoapp"
    # )
    #
    # database = db.cursor()
    # database.execute('SELECT * FROM users')
    # users = database.fetchall()
    # for user in users:
    #     if user[1] == username:
    #         return f"User {username} already exists"


if __name__ == "__main__":
    app.run(debug=True)
