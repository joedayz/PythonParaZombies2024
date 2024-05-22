class Player:
          teamName = 'Liverpool' # Clase variable
          
          def __init__(self, name):
                    self.name = name
                    
          @staticmethod          
          def getTeamName():
                    return Player.teamName
          




print(Player.getTeamName())  #metodos de clase

Carlos = Player("Carlos")
print(Carlos.getTeamName())