class Persona:
          planeta = "Tierra"  #variable de clase
          
          def __init__(self, nombre, edad):
                    self.nombre = nombre  #variables de instancia
                    self.edad = edad  #variables de instancia
                    
          def describir(self):
                    return "Nombre=" + self.nombre + " tiene " + self.edad + " años"
          
class Estudiante(Persona):
          def __init__(self, nombre="-", edad="0", carrera="-"):
                    super().__init__(nombre, edad)
                    self.carrera = carrera
          
          def describir(self):
                    return super().describir() + " y está en la carrera de " + self.carrera + " y estamos en el planeta " + self.planeta
          
class Profesor(Persona):
          def __init__(self, nombre, edad, curso):
                    super().__init__(nombre, edad)
                    self.curso = curso
          
          def describir(self):
                    return super().describir() + " y enseña " + self.curso + " y estamos en el planeta " + self.planeta 
          
#crear objetos          
estudiante = Estudiante("Juan", "20", "Ingenieria en Sistemas")

estudiante.universidad = "UNAM"

profesor = Profesor("Ing. Pedro", "40", "Matematicas")

#invocar a describir

print(estudiante.describir())


print(profesor.describir())



