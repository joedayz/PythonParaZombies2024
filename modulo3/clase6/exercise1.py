class Shape:
          # def __init__(self):
          #           self.sname = "Shape"
          sname = "Shape"          
                    
          def getName(self):
                    return self.sname
          
class XShape(Shape):
          def __init__(self, name):
                    # super().__init__()
                    self.xsname = name
          
          def getName(self):
                    return (super().getName() + ", " + self.xsname)
          
          
myShape = XShape("Circle")
print(myShape.getName())