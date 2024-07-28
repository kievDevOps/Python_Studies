# super()= Function used to give access to the methods of a parent class
# Returns a temporary object of a parent class when used

class Rectangle:

    def __init__(self, lenght, widht):
        self.lenght = lenght
        self.widht = widht

class Square(Rectangle):

    def __init__(self, lenght, widht):
        super().__init__(lenght, widht)

    def area(self):
        return self.lenght*self.widht
    
class Cube(Rectangle):

    def __init__(self, lenght, widht, height):
        super().__init__(lenght, widht)
        self.height = height

    def volume(self):
        return self.lenght*self.widht*self.height
    
square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
