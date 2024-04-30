# ESto es una mala practica de programacion, ya que estamos exponiendo los atributos de la clase
class User:
          def __init__(self, userName=None, password=None):
                    self.__userName = userName
                    self.__password = password
                    
          def login(self, userName, password):
                    if(self.__userName.lower() == userName.lower() and self.__password == password):
                              print("Acceso concedido")
                    else:
                              print("Acceso denegado")
                              
                              
Carlos = User("Carlos", "12345")

Carlos.login("carlos", "12345")


Carlos.__password = "abcde"            # No se puede modificar el atributo privado de esta manera                   

Carlos.login("carlos", "abcde")