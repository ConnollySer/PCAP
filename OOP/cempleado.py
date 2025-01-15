class Empleado: 
    def __init__(self, nombre, apellido, cargo,  salario = 5000):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.__salario = salario
    
    def getSalario(self): 
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre } {self.apellido} trabaja en {self.cargo} y gana {self.getSalario()}"
    
listaEmpleados=[

 Empleado("lolo", "lolore", "chambeando", 25000),
 Empleado("lola", "lolora", "chambeadora"),
 Empleado("lsergio", "connolly", "gili", 452000),
 Empleado("ana", "lolora", "chambeadora", 120)
]

empleados_vip = [empleado for empleado in listaEmpleados if empleado.getSalario() >5000]

for emple in empleados_vip:
    print(emple)