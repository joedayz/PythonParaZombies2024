class Shape:
          def __init__(self):
                    self.sides = 0
          
          def getArea(self):
                    pass

class Rectangle(Shape):
          def __init__(self, width=0, height=0):
                    self.width = width
                    self.height = height
                    self.sides = 4
          
          def getArea(self):
                    return self.width * self.height
          
class Circle(Shape):
          def __init__(self, radius):
                    self.radius = radius
                    self.sides = 0
          
          def getArea(self):
                    return 3.14159 * self.radius ** 2
          
shapes = [Rectangle(6, 10), Circle(7)]

print("Sides de un rectangulo: ", shapes[0].sides)
print("Sides de un ciculo: ", shapes[1].sides)


print("Area de un rectangulo: ", shapes[0].getArea())
print("Area de un ciculo: ", shapes[1].getArea())