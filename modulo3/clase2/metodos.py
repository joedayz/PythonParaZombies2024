class Employee:
          def __init__(self, ID=None, salary=None, department=None):
                    self.ID = ID
                    self.salary = salary
                    self.department = department
                    
          
          def tax(self):
                    return self.salary * 0.3
          
          def salaryPerDay(self):
                    return self.salary / 30


Carlos = Employee(3789, 2500, "Human Resources")
Jose = Employee(3456, 2000, "Marketing")


          
print("Carlos tax: ", Carlos.tax())
print("Jose tax: ", Jose.tax())

print("Carlos salary per day: ", Carlos.salaryPerDay())

print("Jose salary per day: ", Jose.salaryPerDay())          
          
          