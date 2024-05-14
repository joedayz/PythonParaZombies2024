from abc import ABC, abstractmethod

class Shape(ABC):  #Figura
          def __init__(self):
                    self.sides = 0
                    
          @abstractmethod
          def getArea(self):
                    pass

class Rectangle(Shape):
          def __init__(self, width=0, height=0):
                    self.width = width
                    self.height = height
                    self.sides = 4
          
          def getArea(self):
                    return self.width * self.height
          
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def getArea(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

          
class Circle(Shape):
          def __init__(self, radius):
                    self.radius = radius
                    self.sides = 0
          
          def getArea(self):
                    return 3.14159 * self.radius ** 2
          
          
shape = Shape()

rectangle = Rectangle(10, 10)
square = Square(10)
circle = Circle(10)