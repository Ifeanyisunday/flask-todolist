from db_models import db, User


class User_service:
    @staticmethod
    def register_users(username, email, password):
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()


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
        query = 'SELECT * FROM users WHERE username = %s and password = %s'
        values = (username, password)
        database.execute(query, values)
        user = database.fetchone()
        if user[1] == username:
            if user[3] == 0:
                database = mydb.cursor()
                query = 'UPDATE users SET is_logged_in = %s WHERE username = %s'
                values = (1, username)
                database.execute(query, values)
                mydb.commit()
                database.close()
                mydb.close()
                return "you are now logged in"
        else:
            return "User not found or you are offline"
