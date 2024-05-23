class Personaje:
    def __init__(self, nombre, salud=100):
        self.nombre = nombre
        self.salud = salud

    def recibir_danio(self, cantidad):
        self.salud -= cantidad
        if self.salud <= 0:
            print(f"{self.nombre} ha sido derrotado!")

    def salud_actual(self):
        return self.salud

class Heroe(Personaje):
    def __init__(self, nombre, salud=100, poder="fuerza"):
        super().__init__(nombre, salud)
        self.poder = poder

    def usar_poder(self):
        print(f"{self.nombre} utiliza {self.poder} para combatir!")

    def saludar(self):
        print(f"Soy {self.nombre}, el valiente héroe!")
        
class Villano(Personaje):
    def __init__(self, nombre, salud=100, habilidad="malicia"):
        super().__init__(nombre, salud)
        self.habilidad = habilidad

    def usar_habilidad(self):
        print(f"{self.nombre} utiliza {self.habilidad} para causar caos!")

    def saludar(self):
        print(f"Soy {self.nombre}, el temido villano!")
        
        
heroe1 = Heroe("Superman")
villano1 = Villano("Joker")

heroe1.saludar()
villano1.saludar()

heroe1.usar_poder()
villano1.usar_habilidad()        

villano1.recibir_danio(30)
print(f"Salud actual de {villano1.nombre}: {villano1.salud_actual()}")