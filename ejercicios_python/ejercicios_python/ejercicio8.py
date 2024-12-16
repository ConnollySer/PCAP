
n = int(input("Ingresa un número : "))
fac = 1
for i in range(1, n + 1):
    fac *= i
    print("El factorial de", n, "es:", fac)