import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="vitalspring10",
    port='3306',
    database="todoapp"
)

database = db.cursor()
database.execute("SELECT * FROM users")
users = database.fetchall()

for user in users:
    print(user)
    print("username =" + user[1])
    print("email =" + user[2])