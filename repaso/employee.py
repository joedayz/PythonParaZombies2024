class Employee:
          def __init__(self, name, salary):
                    self.name = name
                    self.salary = salary
          
          def display(self):
                    print(f"Name: {self.name}, Salary: {self.salary}")
                    
          def tax(self):
                    return self.salary * 0.2
          
          def salaryPerDay(self):
                    return self.salary / 30
          
          def demo(self, a, b, c, d=5, e=None):
                    print("a", a)
                    print("b", b)
                    print("c", c)
                    print("d", d)
                    print("e", e)
          
          
Jose = Employee("Jose", 1000)  #objeto de la clase Employee

print(Jose.display())
print(Jose.tax())
print(Jose.salaryPerDay())


Jose.demo(1, 2, 3, 4, 5)

Jose.demo(1, 2, 3)