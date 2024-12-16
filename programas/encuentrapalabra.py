# Encuentra la palabra oculta

palabra = input("Dame una palabra a buscar: ").upper()
grupo = input("Introduce grupo de caracteres: ").upper()

palabra_encontrada = True
posicion = 0

for c in palabra:
    pos = grupo.find(c, posicion)
    if pos < 0:
        palabra_encontrada = False
        break
    posicion = pos + 1

if palabra_encontrada:
    print("La palabra se encuentra en el grupo de caracteres")
else:
    print("La palabra no se encuentra en el grupo de caracteres")