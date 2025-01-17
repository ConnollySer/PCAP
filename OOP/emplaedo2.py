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
            
    def getSalrio(self):
        return self.__salario
    
    def __repr__(self):
        return f"Empleado('{self.nombre}','{self.cargo}', {self.getSalrio()})"
    
empleado1 = Empleado("juan", "chambero")
empleado2 = Empleado("juan", "chambero", 30000)


for trabajdor in Empleado.plantilla:
    print(trabajdor)
    