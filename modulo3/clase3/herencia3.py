class Vehicle:
          def setToSpeed(self, speed):
                    self.speed = speed
                    print("Speed is set to", speed)
                    
                    
class Car(Vehicle):
          def openTrunk(self):
                    print("Trunk is now open.")                    
                    
                    
corolla = Car()

corolla.setToSpeed(50)
corolla.openTrunk()

