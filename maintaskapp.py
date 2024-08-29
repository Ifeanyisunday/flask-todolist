from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from services.user_service import User_service
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vitalspring10@127.0.0.1/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
Bootstrap(app)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#     tasks = db.relationship('Task', backref='user', lazy=True)
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), unique=True, nullable=False)
#     note = db.Column(db.Text, nullable=False)
#     done = db.Column(db.Boolean, default=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     def __repr__(self):
#         return '<Task %r>' % self.title
#
#
# db.create_all()
# @app.route('/')
# def index():
#     tasks = Task.query.all()
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = User.query.filter_by(username=username).first()
#         if user and user.password == password:
#             return redirect(url_for('index'))
#
#
# @app.route('/logout')
# def logout():
#     db.session.delete(User)
#     db.session.commit()
#     return redirect(url_for('login'))
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = User.query.filter_by(username=username).first()
#         if user:
#             return redirect(url_for('login'))
#
# @app.route('/tasks', methods=['GET', 'POST'])
# def tasks():
#     tasks = Task.query.all()
#
#
# @app.route('/tasks/<int:task_id>', methods=['GET', 'POST'])
# def task(task_id):
#     task = Task.query.filter_by(id=task_id).first()
#     if request.method == 'POST':
#         title = request.form.get('title')
#         description = request.form.get('description')
#         done = request.form.get('done')
#         user = User.query.filter_by(id=task.user_id).first()
#         if done:
#             db.session.delete(task)
#             db.session.commit()
#             return redirect(url_for('index'))
#
#
# @app.route('/tasks/<int:task_id>', methods=['GET', 'POST'])
# def task_done(task_id):
#     task = Task.query.filter_by(id=task_id).first()
#     done = request.form.get('done')
#     user = User.query.filter_by(id=task.user_id).first()
#     if done:
#         db.session.delete(task)
#         db.session.commit()
#         return redirect(url_for('index'))
#
# @app.route('/tasks/<int:task_id>', methods=['GET', 'POST'])
# def task_done(task_id):
#     task = Task.query.filter_by(id=task_id).first()
#     done = request.form.get('done')
#     user = User.query.filter_by(id=task.user_id).first()
#     if done:
#         db.session.delete(task)
#         db.session.commit()
#         return redirect(url_for('index'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#     db.create_all()
#     User_service()



# db = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     passwd="vitalspring10",
#     port='3306',
#     database="todoapp"
# )


# mydatabase = db.cursor()
# mydatabase.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, is_logged_in INT DEFAULT 1)")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # user_validation(username, password)

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


#
# @app.route("/login", methods=['POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user_validation(username, password)
#
#         try:
#             if username and password:
#                 user_service = User_service()
#                 user_service.login_user(username, password)
#                 return render_template('taskdashboard.html')
#         except Exception as message:
#             return f'Error: {message}'
#     else:
#         return redirect(url_for('loginhtml'))
#
#
# def user_validation(username, password):
#     if username == "" or password == "":
#         return "Please fill all fields"
#     elif username == "  " or password == "   ":
#         return "Please fill all fields"
#
#     # db = mysql.connector.connect(
#     #     host="127.0.0.1",
#     #     user="root",
#     #     passwd="vitalspring10",
#     #     port='3306',
#     #     database="todoapp"
#     # )
#     #
#     # database = db.cursor()
#     # database.execute('SELECT * FROM users')
#     # users = database.fetchall()
#     # for user in users:
#     #     if user[1] == username:
#     #         return f"User {username} already exists"


if __name__ == "__main__":
    app.run(debug=True)
