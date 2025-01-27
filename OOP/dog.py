class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: ¡Guau!"
 
 
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, Corderito!"
 
 
class GuardDog(SheepDog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, Señor Intruso!"
    
class LowlandDog(SheepDog):
	def __str__(self):
		return Dog.__str__(self) + " ¡No me gustan las montañas!"
 
paco = LowlandDog("Chiguagua")
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
print("-------------------")
print(rocky)
print(luna) 
print("-------------------")
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))
print("-------------------")
print(luna is luna, rocky is luna)
print(rocky.kennel)
print("-------------------")
print(paco)
 