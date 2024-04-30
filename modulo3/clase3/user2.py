class User:
          def __init__(self, userName=None, password=None):
                    self.userName = userName
                    self.password = password
                    
          def login(self, userName, password):
                    if(self.userName.lower() == userName.lower() and self.password == password):
                              print("Acceso concedido")
                    else:
                              print("Acceso denegado")
                              
Carlos = User("Carlos", "12345")

Carlos.login("carlos", "12345")

Carlos.login("Carlos", "1234512341341")

Carlos.password = "abcde"

Carlos.login("Carlos", "abcde")
