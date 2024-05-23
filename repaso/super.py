class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")
        
class Car(Vehicle):  # defining the child class
    def display(self):  # defining display method in the child class
        #super().display()  # calling the display method of the parent class
        print("I am from the Car Class")
        
obj = Car()
obj.display()  # calling the display method of the child class