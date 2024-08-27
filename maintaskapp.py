from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

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
# mydatabase.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, is_logged_in BOOLEAN DEFAULT FALSE)")

# class SimpleMiddleware:
#     def __init__(self, wsgi_app):
#         self.wsgi_app = wsgi_app
#
#     def __call__(self, environ, start_response):
#         # Do something before passing the request to the next WSGI application
#         print("Before passing to the next app")
#
#         # Call the next WSGI application or middleware
#         response = self.wsgi_app(environ, start_response)
#
#         # Do something after the response from the next app
#         print("After passing to the next app")
#
#         return response
@app.route("/")
def hello_world():
    return render_template('signup.html')


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            try:
                db = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    passwd="vitalspring10",
                    port='3306',
                    database="todoapp"
                )

                database = db.cursor()
                database.execute('INSERT INTO users (username, password) VALUES (%s %s)', (username, password))
                db.commit()
                database.close()
                db.close()
                return redirect(url_for('submit'))
            except Exception as e:
                return f'Error: {e}', 500
    return render_template('task.html')


if __name__ == "__main__":
    app.run(debug=True)
