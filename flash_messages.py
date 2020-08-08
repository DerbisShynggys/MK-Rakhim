class Flash_Messages():

    def __init__(self):
        self.connection =psycopg2.connect(
        database="postgres",
        user="postgres",
        password="",
        host="127.0.0.1",
        port="5432"
        )

        self.cursor = self.connection.cursor()


    def set_flash_message(self, key, message):
        with self.connection:
            self.cursor.execute("INSERT INTO users (email, password) "
                                "VALUES ('"+ key + "', '" + message + "')")


    def display_message(self, key):
        with self.connection():
            self.cursor.execute("SELECT * FROM flash_messages WHERE key = '" + key + "'")
            result = self.cursor.fetchall()

            return result

    def close(self):
        self.connection.close()
