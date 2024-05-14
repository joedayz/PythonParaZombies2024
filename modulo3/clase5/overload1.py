class Com:
          def __init__(self, real=0, imag=0):
                    self.real = real
                    self.imag = imag
                    
          def __add__(self, other):
                    temp = Com(self.real + other.real, self.imag + other.imag)
                    return temp
          
          def __sub__(self, other):
                    temp = Com(self.real - other.real, self.imag - other.imag)
                    return temp
          
          # __truediv__  para /
          # __mul__ para *
          #__lt__ para <
          #__gt__ para >
          #__eq__ para ==
          
obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("Real de obj3: ", obj3.real)
print("Imag de obj3: ", obj3.imag)
print("Real de obj4: ", obj4.real)
print("Imag de obj4: ", obj4.imag)