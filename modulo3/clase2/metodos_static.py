class Player:
          planetName = "Tierra"  #variable de clase
          
          
          def __init__(self, name):
                    self.name = name #variable de instancia
                    
          @staticmethod          
          def demo():
                    print("This is a static method")
          
          
# Los metodos static si se pueden llamar con objetos o clase

carlos = Player("Carlos")
carlos.demo()

Player.demo()