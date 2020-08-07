# Task 4

my_tasks = {'indicator': 'My Tasks', 'color': 'black', 'score': '130', 'max_score': '500'}
transfered = {'indicator': 'Transfered', 'color': 'green', 'score': '440 TB', 'max_score': '1000 TB'}
bugs = {'indicator': 'Bugs Squashed', 'color': 'blue', 'score': '77%', 'max_score': '100%'}
test = {'indicator': 'User Testing', 'color': 'violet', 'score': '7 days', 'max_score': '10 days'}


info = []
info.append(my_tasks)
info.append(transfered)
info.append(bugs)
info.append(test)


class Show():

    def show_indicator(self, dict):
        self.dict = dict

        for indicator in dict:
            for key, value in indicator.items():
                #                 Здесь типа реализация некой функции по отображению данных в виде индикаторов
                print(key, ': ', value)
            print('\n')


showIndicator = Show()
showIndicator.show_indicator(info)
