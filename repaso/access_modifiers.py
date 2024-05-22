class Employee:
          def __init__(self, name, salary):
                    self.name = name
                    self.__salary = salary
                    
          def __displayID(self):
                    print("ID: 123456")
                    

Carlos = Employee("Carlos", 1000)  #objeto de la clase Employee
print(Carlos.name)
# print(Carlos.__salary)

Carlos.__displayID()
