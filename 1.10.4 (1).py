class Volunteers:
    status = "Волонтер"
    def __init__(self, firstname,lastname, city):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city


class Mentor(Volunteers):
    status = "Наставник"

class Professor(Mentor):
    status = "Профессор"

class Student(Volunteers):
    status = "Студент"



v1 = Mentor("Иван","Иванов","Москва")
v2 = Professor ("Петр","Петров","Тверь")
v3 = Student("Олег","Николаев","Псков")
v4 = Mentor("Николай","Иванов","Москва")
v5 = Student("Дмитрий","Смирнов","Казань")
v6 = Professor ("Михаил","Михайлов","Тула")


Volunteer = [v1,v2,v3,v4,v5,v6]



def info():
    ask_guests = int(input("Выберите гостей: 1- весь список гостей , 2- наставник, 3- профессор, 4-студент: "))
    for v in Volunteer:
        if ask_guests == 1:
            print(v.firstname + " " + v.lastname +", г."+ v.city + "," + "статус:" +v.status)
        elif ask_guests == 2:
            print(v1.firstname + " " + v1.lastname +", г."+ v1.city + "," + "статус:" +v1.status)
            print(v4.firstname + " " + v4.lastname + ", г." + v4.city + "," + "статус:" + v4.status)
            break
        elif ask_guests == 3:
            print(v2.firstname + " " + v2.lastname +", г."+ v2.city + "," + "статус:" +v2.status)
            print(v6.firstname + " " + v6.lastname + ", г." + v6.city + "," + "статус:" + v6.status)
            break
        elif ask_guests == 4:
            print(v3.firstname + " " + v3.lastname +", г."+ v3.city + "," + "статус:" + v3.status)
            print(v5.firstname + " " + v5.lastname + ", г." + v5.city + "," + "статус:" + v5.status)
            break
        else:
            print("Неправильный ввод!")
            break

    return info()


info()



















