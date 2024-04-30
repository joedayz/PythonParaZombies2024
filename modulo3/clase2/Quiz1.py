# obj = Calculator(10, 94);
#obj.add()
#obj.subtract()
#obj.multiply()
#obj.divide()



#output

#104
#84
#940
#9.4

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1 + self.num2)

    def subtract(self):
        return (self.num1 - self.num2)

    def multiply(self):
        return (self.num1 * self.num2)

    def divide(self):
        return (self.num1 / self.num2)
    
    
obj = Calculator(10, 94);
print("Suma:", obj.add())
print("Resta:", obj.subtract())
print("Multiplicacion:", obj.multiply())
print("Division:", obj.divide())