# task 5

class User(object):

    def __init__(self, name, spec, role, mail, status):
        self.name = name
        self.spec = spec
        self.role = role
        self.mail = mail
        self.status = status


Sunny = User('Sunny A.', 'UI/UX Expert', 'Lead Author', '@myplaneticket', 'True')
Jos = User('Jos K.', 'ASP.NET Developer', 'Partner & Contributer', '@atlantez', 'True')
Johanni = User('Johanni L.', 'PHP Developer', 'Partner & Contributer', '@lodev09', 'True')
Roberto = User('Roberto R.', 'Ralls Developer', 'Partner & Contributer', '@sildur', 'True')

users = []
users.append(Sunny)
users.append(Jos)
users.append(Johanni)
users.append(Roberto)


class Show():

    def show_list(self, users):

        self.users = users
        active_users = []
        banned_users = []

        for user in users:
            if user.status == 'True':
                active_users.append(user)
            else:
                banned_users.append(user)

        print('Active users:')
        for active in active_users:
            print(active.name, active.spec, active.role, active.mail, active.status)

        print('Banned users:')
        for ban in banned_users:
            print(ban.name, ban.spec, ban.role, ban.mail, ban.status)


list_user = Show()
list_user.show_list(users)