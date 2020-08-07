# Task_1
filter_list = ['Reports', 'Analytics', 'Export', 'Storage']


class Show:
    def showlist(self, list):
        self.list = list

        for unit in list:
            print(unit)


search = Show()
search.showlist(filter_list)