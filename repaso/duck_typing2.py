class Dog:
    def Speak(self):
        print("Woof woof")
        
class Cat:
    def Speak(self):
        print("Meow meow")
        
class Dragon:
          def Go(self):
                    print("Raafffff")        

class AnimalSound:
    def Sound(self, animal):
        animal.Speak()        
        
        
sound = AnimalSound()

dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)

# dragon = Dragon()
# sound.Sound(dragon)  # AttributeError: 'Dragon' object has no attribute 'Speak'