# Public attributes
# Que se puede acceder desde dentro y fuera de la clase

class Employee:
          def __init__(self, ID=None, salary=None, department=None):
                    self.ID = ID
                    self.__salary = salary  # esta variable salary se ha vuelto privada
                    self.department = department
                    
          def displaySalary(self):  # displaySalary is a public method
                    print("Salary:", self.__salary)                    
          
          def displayID(self):
                    print("ID: ", self.ID)
                   
                    
                    
Steve = Employee(3789, 2500, "Human Resources")
Steve.displayID()

#print("Salary = ", Steve.__salary)  # AttributeError: 'Employee' object has no attribute '__salary'

Steve.displaySalary()  # Salary: 2500