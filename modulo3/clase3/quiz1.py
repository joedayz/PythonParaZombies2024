# propiedades
# name y rollNumber



class Student:
    __name = None 
    __rollNumber = None
    
    def setName(self, name):
        self.__name = name 

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
    
# create objetos Student y prueba todos esos metodos    

leo = Student()
leo.setName("Leo")
print("Name = ", leo.getName())
leo.setRollNumber(123)
print("Roll Number = ", leo.getRollNumber())