from db import DB
from redirect import Redirect as redir
from messages import Flash_messages as message

db = DB()


class Registration():

    def register(self, email, password):
        self.email = email
        self.password = password

        user_id = db.get_user_by_email(email, password)
        if bool(user_id) is False:
            db.add_user(email, password)
            message.flash_message(self, key='success_reg')
            redir.redir_log_page(self)
        elif bool(user_id) is True:
            message.flash_message(self, key='exists')
        else:
            print('Error')
