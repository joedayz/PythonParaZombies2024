class Player:
          teamName = 'Alianza lima'  #variable de clase
          
          def __init__(self, name):
                  self.name = name  #variable de instancia
                  
p1 = Player("Carlos")
p2 = Player("Leonardo")


print("Name: ", p1.name)
print("Team Name: ", p1.teamName);

print("Name: ", p2.name)
print("Team Name: ", p2.teamName);