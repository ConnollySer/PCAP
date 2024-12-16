
import random

print("Adivina un número entre el 1 y el 100")
numeroAleatorio = random.randint(1, 100)
intento = 0
acertado = False  
print(numeroAleatorio)

while not acertado:  
    numer = int(input("Introduce un número: "))
    intento += 1
    if numer == numeroAleatorio:
        print(f"Has acertado y lo has conseguido en {intento} intentos")
        acertado = True  
        
    elif numer > numeroAleatorio:
        print("El número que busco es menor")
        
    elif numer < numeroAleatorio:
        print("El número que busco es mayor")
        
    else:
        print("No se puede comparar los números")
        