fecha = ''

while True:
    fecha = input("Introduce tu fecha de cumpleaños (En formato AAAAMMDD): ")
    if fecha.isnumeric() and len(fecha) == 8: 
        break
    print("Debes introducir una fecha en formato AAAAMMDD")

digito = 0
suma = 0


for char in fecha:
    suma += int(char)


while suma > 9:
    digito = 0
    for c in str(suma):
        digito += int(c)
    suma = digito

print("Tu número de vida es", suma)