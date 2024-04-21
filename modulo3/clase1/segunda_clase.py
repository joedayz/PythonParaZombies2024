class Employee:
          def __init__(self, ID=None, salary=0, department=None):
                    self.ID = ID
                    self.salary = salary
                    self.department = department
    
    



leonardo = Employee(1234, 5000, 'Human Resources')

carlos = Employee(4567, 6000, "Administration")

jose = Employee()

print("Leonardo:")
print("ID =", leonardo.ID)
print("Salary", leonardo.salary)
print("Department:", leonardo.department)
leonardo.title = "Manager"
print("Title:", leonardo.title)

print("Carlos:")
print("ID =", carlos.ID)
print("Salary", carlos.salary)
print("Department:", carlos.department)

print("Jose:")
print("ID =", jose.ID)
print("Salary", jose.salary)
print("Department:", jose.department)