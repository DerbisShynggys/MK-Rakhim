from db import DB
from flask import Flask, render_template

request_to_base = DB()

# Необходимо настроить среду для запуска Редирект
app = Flask(__name__)

class Redirect():

    def redirect(self, path):

        self.path = path

        @app.route('/' + str(path))
        def page():
            return render_template('/' + str(path) + '.html')


email = input('Input email: ')
password = input('Input password: ')

result = request_to_base.get_user_by_email(email, password)
print(result)

# Нужно настроить среду для Flask
# if __name__ == '__main__':
#     app.run(debug=True)
