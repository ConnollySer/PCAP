def read_int(prompt, min, max):
    verdad = False
    while not verdad:
        try:
            num = int(input(prompt))
            verdad = True
        except ValueError:
            print("Error: entrada incorrecta")
        if verdad:
            verdad = num >= min and num <= max
        if not verdad:
            print("Error: el valor no está dentro del rango permitido")
    return num;


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)