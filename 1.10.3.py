class User:
    def __init__(self,first_name,second_name,balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance

    def get_information(self):
        return "Клиент :"+ self.first_name + " " + self.second_name + "." + "Баланс: "+ str(self.balance) + "pyб"


class Info:
    def __init__(self):
        self.data = []

    def add_user(self, first_name, second_name,balance):
        user = User(first_name,second_name, balance)
        return self.data.append(user)

    def find_users(self, first_name):
        info_list = []
        for user in self.data:
            if user.first_name == first_name:
                info_list.append(user.get_information())
        return info_list


users_db = Info()

def result():
    number = int(input("Вы зашли в электроный кошелек!\nНажмите 1, если хотите добавить клиента в базу:\nНажмите 2, "
                       "если хотите вывести информацию о клиенте :"))
    if  number == 1:
        users_db.add_user(input("Введите Имя: "),input("ведите фамилию: "),int(input("Введите баланс: ")))
        result()
    elif number == 2:
        print(users_db.find_users(input("Введите Имя: ")))
        result()
    else:
        print("Ошибка! Введите число 1 или 2")
        result()

result()



