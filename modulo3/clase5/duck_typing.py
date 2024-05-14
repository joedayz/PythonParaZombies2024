# Que PYthon nos permite usar cualquier objeto que provea el comportamiento requerido
# sin necesidad de ser una subclase de una clase especifica. Esto se llama duck typing.

class Dog:
          def speak(self):
                    print( "Woof!")
          
class Cat:
          def speak(self):
                    print("Meow!")
                    
class Joe:
          def name(self):
                    print("JoeDayz!")
          
class AnimalSound:
          def sound(self, animal):
                    animal.speak()
                    
                    
sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.sound(dog)
sound.sound(cat)

#joe = Joe()

#sound.sound(joe) # AttributeError: 'Joe' object has no attribute 'speak'