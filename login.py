from db import DB
from redirect import Redirect as redir
from messages import Flash_messages as message

db = DB()


class Login():

    def login(self, email, password):

        user = db.get_user_by_email(email, password)

        if user:
            Login.validation(self, user, email, password)
        elif not user:
            message.flash_message(self, 'user not exists')
        else:
            print('Error')

    def validation(self, user, email, password):
        if user[0][1] == email:
            print('User exists')
            if user[0][2] == password:
                redir.redir_main_page(self)
                return [user]
            else:
                message.flash_message(self, 'wrong pass')
        else:
            print('error')
