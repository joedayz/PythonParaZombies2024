class User:
          def __init__(self, username=None):
                    self.__username = username
                    
          def setUsername(self, x):      #setter
                    self.__username = x
                    
          def getUsername(self):  #getter
                    return self.__username          
          
          
Carlos = User("Carlos")

#Carlos.username = "Pepito"

print("Before: " ,Carlos.getUsername())          


Carlos.setUsername("Juan")

print("After: " ,Carlos.getUsername())