# Task_3

main = 'https://www.mysite.kz/main'
php = 'https://www.mysite.kz/main/php'
func = 'https://www.mysite.kz/main/php/func/'

path = {'Главная': main, 'PHP': php, 'Функции': func}


class Location():
    def current_location(self, dict):
        self.dict = dict
        i = 0
        keys = list(dict.keys())
        values = list(dict.values())

        while i < len(keys):
            if i == len(keys) - 1:
                print(keys[i])
            else:
                print(keys[i], end=' / ')
            i += 1


location = Location()
location.current_location(path)