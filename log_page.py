from login import Login


email = input('Login: ')
password = input('Password: ')

log = Login()

session = log.login(email, password)

print('Данные сессии: ', session)




