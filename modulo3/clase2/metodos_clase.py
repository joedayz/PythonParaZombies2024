class Player:
          planetName = "Tierra"  #variable de clase
          
          
          def __init__(self, name):
                    self.name = name #variable de instancia
                    
          @classmethod          
          def getPlanetName(cls):
                    return cls.planetName 
          
          
print(Player.getPlanetName())

# carlos = Player("Carlos")
# carlos.getPlanetName()