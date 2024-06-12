# Sobrecarga de OPERADORES (+, -, *, /, <, >, ==)

# a = 3 + 7
# b = "abc" + "def"


class Com:
          def __init__(self, real=0, imag=0):
                    self.real = real
                    self.imag = imag
          
          def __add__(self, other):  # sobrecarga del operador +
                    temp = Com(self.real + other.real, self.imag + other.imag)
                    return temp
          
          def __sub__(self, other):
                    temp = Com(self.real - other.real, self.imag - other.imag)
                    return temp
                    
          
          
obj1 = Com(3, 7)

obj2 = Com(2, 5)

obj3 = obj1 + obj2

print(obj3.real)  # Com(5, 12)
print(obj3.imag)  # Com(5, 12)

obj4 = obj1 - obj2
print(obj4.real)  # Com(1, 2)
print(obj4.imag)  # Com(1, 2


#Operator	Method
#+	__add__ (self, other)
#-	__sub__ (self, other)
#/	__truediv__ (self, other)
#*	__mul__ (self, other)
#<	__lt__ (self, other)
#>	__gt__ (self, other)
#==	__eq__ (self, other)