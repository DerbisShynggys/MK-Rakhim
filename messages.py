

class Flash_messages():

    def __init__(self):
        self.key = self.key

    def flash_message(self, key):
        if key == 'success_reg':
            print('Пользователь успешно зарегистрирован')
        elif key == 'exists':
            print('Пользователь уже зарегистрирован')
        elif key == 'wrong pass':
            print('Пароль не совпадает')
        elif key == 'user not exists':
            print('Пользователь не существует')
