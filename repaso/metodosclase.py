class Player:
          teamName = 'Liverpool' # Clase variable
          
          def __init__(self, name):
                    self.name = name
                    
          @classmethod          
          def getTeamName(cls):
                    return cls.teamName
          




print(Player.getTeamName())  #metodos de clase

Carlos = Player("Carlos")
print(Carlos.getTeamName())