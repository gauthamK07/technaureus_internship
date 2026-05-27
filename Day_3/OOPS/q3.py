from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.__radius = radius
    def area(self):
        return 3.14*self.__radius*self.__radius

class Rectangle(shape):
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length*self.__width

class square(shape):
    def __init__(self,side):
        self.__side = side
    def area(self):
        return self.__side*self.__side

class triangle(shape):
    def __init__(self,base,height):
        self.__base = base
        self.__height = height
    def area(self):
        return 0.5*self.__base*self.__height

print("Area of circle:",circle(10).area())
print("Area of Rectangle:",Rectangle(10,20).area())
print("Area of Square:",square(10).area())
print("Area of Triangle:",triangle(10,20).area())
