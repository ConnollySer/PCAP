# 1º ejercicio
print("hola mundo")

# 2º Ejercicio

num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicacion es: ", multiplicacion)
print("La division es: ", division)

#3º Ejerccio
print("el número por acertar esta entre el 1 y el 10")
correcto = 5
vez = 1 
while vez != 0:
    numero = int(input("ingrese un número: "))
    if numero == correcto:
        print("acertaste")
        break;
    else:
        print("No te quedan intentos")
        vez = vez -1
        break;
    
        #10 intentos
print("el número por acertar esta entre el 1 y el 10")
numeroCorrecto=10
vez=10
while vez != 0:
    numero = int(input("ingrese un número: "))
    if numero == numeroCorrecto:
        print ("Acertaste")
        break;
    else:
        print("Sigue intentandolo")
        vez = vez -1
        
    #infinito
print("el número por acertar esta entre el 1 y el 10")
numAcer =6
bucle = True

while bucle == True:
    numero = int(input("Ingrese un número: "))
    if numero == numAcer:
        print("Acertaste")
        break;
    else:
        print("Sigue intentandolo")
        
        
# 4º Ejercicio

list = []
list.append(1)
list.append(15)
list.append("hola")
list.append("h")

print(list)

list.pop()
print(list)

list.append("nuevo_añadidio")
print(list)

list.clear()
print(list)

# 5º Ejercicio
cont = 0
for i in range (1,11):
    cont += 1
    print(f"Este bucle va por la vuelta:  {cont}")
    
    
# 6º Ejercio
number1 = float(input("Dame un numero: "))
number2 = float(input("Dame otro numero: "))

if number1 < number2:
    print(f"El primer número {number1} es menor que el segundo {number2}")
elif number2 > number1:
    print(f"El segundo número {number2} es mayor que el primero {number1}")
elif number1 == number2:
    print("Los dos números son iguales")
else:
    print("No se puede comparar los números")
    
# 7º ejercicio

paroimpar = int(input("Introduce un número y te digo si es par o impar: "))
if paroimpar % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
# 8º Ejercicio

n = int(input("Ingresa un número : "))
fac = 1
for i in range(1, n + 1):
    fac *= i
    print("El factorial de", n, "es:", fac)
    
#9º Ejercicio

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
        
        
# 10 Ejercicio

def opcionMaquina():
    opciones = ["piedra", "papel", "tijera"]
    eleccion = random.choice(opciones)
    return eleccion

def opcionJugador():
    opcionjugador = input("Elige piedra, papel o tijera: ").lower()
    return opcionJugador

