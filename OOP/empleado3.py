class Empleado:
    plantilla= []
    numeroEmpleado = 0
    def __init__(self, nombre: str, cargo: str, salario = 25000):
        if salario < 0:
            raise ValueError
        else:   
            self.nombre = nombre
            self.cargo = cargo
            self.__salario = salario
            Empleado.plantilla.append(self)
            Empleado.numeroEmpleado += 1
    
        #método estático
    @staticmethod
    def is_integer(num):
        #cuenta el nº de elementos  que tienen punto cer (.0)
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    
        
            

    
    def getSalrio(self):
        return self.__salario
    
    
    #def __repr__(self):
        return f"Empleado('{self.nombre}','{self.cargo}', {self.getSalrio()})"
    
empleado1 = Empleado("juan", "chambero")
empleado2 = Empleado("juana", "chambera", 30000)


for trabajador in Empleado.plantilla:
    print(trabajador)
    
print(Empleado.plantilla)

num1 = 7
num2 = 7.0
num3 = 7.5


if Empleado.is_integer(num1):
    print(f"{num1} es un número entero")
else:
    print(f"{num1} no es un número entero")
if Empleado.is_integer(num2):
    print(f"{num2} es un número entero")
else:
    print(f"{num2} no es un número entero")
if Empleado.is_integer(num3):
    print(f"{num3} es un número entero")
else:
    print(f"{num3} no es un número entero")