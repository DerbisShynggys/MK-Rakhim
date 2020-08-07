# Task_2

privacy = 'Your privacy is important for us and SmartAdmin...'
cookies = 'We collect certain data through cookies and similar technologies'
message = {'Privacy': privacy, 'Cookies and other similar technologies': cookies}


class Show():
    def showmessage(self, dict):
        self.dict = dict

        for key, value in dict.items():
            print(key, end='\n\n')
            print(value, end='\n\n\n')


show = Show()
show.showmessage(message)