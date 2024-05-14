class Vehicle:
          def display(self):
                    print("I am a Vehicle class")
                    
class Car(Vehicle):
          def display(self):
                    super().display()
                    print("I am a Car class")
                    

obj = Car()
obj.display()