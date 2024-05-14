class ParentClass:
          def __init__(self, a, b):
                    self.a = a
                    self.b = b
                    

class ChildClass(ParentClass):
          def __init__(self, a, b, c):
                    super().__init__(a, b)  # inicializa las variables de la clase padre
                    self.c = c    
                    
obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)      