class User:
          def __init__(self, username, password):
                    self.__username = username
                    self.__password = password
                    
          def login(self, username, password):
                    if username == self.__username and password == self.__password:
                              print("Login successful for user: ", self.__username.lower())
                    else:
                              print("Invalid credentials for user: ", self.__username.lower())
                              
Carlos = User("Carlos", "1234")

Carlos.login("Carlos", "abcd")


Jose = User("Jose", "1234")
Jose.login("Jose", "1234")

print(Jose.__password)  # AttributeError: 'User' object has no attribute '__password'

