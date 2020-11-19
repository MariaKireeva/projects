class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


rec_1 = Rectangle(3,5)

print(rec_1.__str__())
print(type(rec_1.__str__()))

