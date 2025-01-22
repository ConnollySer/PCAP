class Humano:
    planeta = 'tierra'
    def __init__(self, nombre):
        self.nombre = nombre

class Saiyan:
    platena = 'saldana'
    def __init__(self, nombre):
        self.nombre = nombre
        
class Mestizo (Humano,Saiyan):
    def __init__(self,nombre, a, b):
       self.progenitor1 =a.nombre
       self.progenitor2 = b.nombre
       self.nombre = nombre
   
   #para ver las superclases se usa bases
    def verAncestros(self):
        for x in Mestizo.__bases__:
            print(x.__name__, end= ' ')
        print()


goku = Saiyan("Kakaroto")
vegeta = Saiyan("Vegeta")
bulma = Humano("bulma")
trunks = Mestizo('trunks',vegeta, bulma )

#da el tipo de objeto 

print(type(trunks).__name__)
print(type(goku).__name__)
print(type(bulma).__name__)
print(type(vegeta).__name__)

#saca todo ( atributo y metodos) lo que tiene la clase en calve / valor
print(trunks.__dict__)
#con este atrinbuto usando el nombre del a
print(f"La mama de trunks es  {trunks.__dict__['progenitor2']}")

#  me dice el modulo donde se esta ejecuntando el codigo 
print(trunks.__module__)


trunks.verAncestros()
print(trunks.planeta)

if type(trunks).__name__ == "Mestizo":
    if issubclass(Mestizo, Saiyan):
        print(f"{trunks.nombre} Es Saiyan ")
        if issubclass(Mestizo, Humano):
            print(f"{trunks.nombre} Es Humano")
    else:
        print("No es Saiyan ni humano")
        
    
print(isinstance(trunks, Humano))

 