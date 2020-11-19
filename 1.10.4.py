class Guest:
    def __init__(self, first_name, second_name, city, status):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.status = status

    def get_information(self):
        return "Гость :"+ self.first_name + " " + self.second_name + "." + "Город: "+ self.city + \
               "Статус:" + self.status


class Info(Guest):
    def __init__(self, first_name, second_name, city, status):
        super().__init__(first_name,second_name,city,status)
        self.data = []




    def add_user(self, first_name, second_name,city, status):
        user = Info(first_name, second_name, city,status)
        self.data.append(user)
        return self.data



users_db = Info("", "", "", "")

def result():
    input("Добавьте гостя в список:")
    users_db.add_user(input("Введите Имя: "),input("ведите фамилию: "),
                       input("Введите город: "), input("Введите статус:"))


result()


