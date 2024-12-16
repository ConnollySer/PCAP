import math
try:
    x = float(input("Ingresa un número: "))
    assert x >= 0.0
except AssertionError:
    print("El número no es positivo")
    exit(1)
    
x = math.sqrt(x)

print(x)
    