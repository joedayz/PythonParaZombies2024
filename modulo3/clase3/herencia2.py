class Vehicle:
          def __init__(self, make, color, model):
                    self.make = make
                    self.color = color
                    self.model = model
                    
                    
          def printDetails(self):
                    print("Manufacturer:", self.make) 
                    print("Color:", self.color)   
                    print("Model:", self.model)          
                    
class Car(Vehicle):
          def __init__(self, make, color, model, doors):
                    Vehicle.__init__(self, make, color, model)
                    self.doors = doors

          def printCarDetails(self):
                    self.printDetails()
                    print("Doors:", self.doors)
                    
                    
                    
carJoe = Car("Jetour", "Blanco", "X70", 4)

carJoe.printCarDetails()                    