class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return '(({}, {}),{}, {}))'.format(self.x, self.y,self.width,self.height)


rec_1 = Rectangle(40,30,7,9)

print(rec_1.__str__())
print(type(rec_1.__str__()))

