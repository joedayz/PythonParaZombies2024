class Player:
          planeta = "Tierra"  #variable de clase
          teamName = 'Alianza lima'  #variable de clase
          
          def __init__(self, name):
                  self.name = name  #variable de instancia
                  
p1 = Player("Farfan")
p2 = Player("Guerrero")


print("Name: ", p1.name)

print("Team Name: ", p1.teamName)
print(p1.planeta)

print("Name: ", p2.name)

print("Team Name: ", p2.teamName)
print(p2.planeta)

Player.teamName = "Vallejo"

print("Team Name: ", p2.teamName)


print("Team Name: ", p1.teamName)