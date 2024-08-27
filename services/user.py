import mysql


class User_service:

    @staticmethod
    def register_users(username, password):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="vitalspring10",
            port='3306',
            database="todoapp"
        )

        database = mydb.cursor()
        database.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mydb.commit()
        database.close()
        mydb.close()


    @staticmethod
    def find_user(username):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="vitalspring10",
            port='3306',
            database="todoapp"
        )

        database = mydb.cursor()
        query = 'SELECT * FROM users WHERE username = %s'
        values = (username)
        database.execute(query, values)
        users = database.fetchall()
        for user in users:
            if user[3] == 0:
                return user

    @staticmethod
    def login_user(username, password):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="vitalspring10",
            port='3306',
            database="todoapp"
        )

        database = mydb.cursor()
        query = 'UPDATE users SET is_logged_in = %s WHERE user_id = %s'
        values = (1, username)
        database.execute(query, values)
        mydb.commit()
        database.close()
        mydb.close()
