import psycopg2


class DB():

    def __init__(self):
        self.connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="",
            host="127.0.0.1",
            port="5432"
        )

        self.cursor = self.connection.cursor()

    def get_user_by_email(self, email, password):
        self.email = email
        self.password = password

        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE email = '" + email + "'")
            result = self.cursor.fetchall()
            return result
            # if not result:
            #     id = DB.add_user(self, email, password)
            #     return True
            # elif result:
            #     return result



    def add_user(self, email, password):
        self.email = email
        self.password = password

        with self.connection:
            self.cursor.execute("INSERT INTO users (email, password) "
                                "VALUES ('" + email + "', '" + password + "')")
            self.cursor.execute("SELECT id FROM users WHERE email = '" + email + "'")
            result = self.cursor.fetchall()

        return result[0][0]

    def close(self):
        self.connection.close()
