while True:
    fecha = input("Dame tu dfecha de nacimiento en formato AAAAMMDD ")
    if fecha.isnumeric():
        break
    print("El formato no es corrcto")
    
digito = 0
suma = 0

for char in fecha:
    digito = int(char)
    suma = suma + digito
    print(suma)