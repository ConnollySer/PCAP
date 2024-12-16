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
    