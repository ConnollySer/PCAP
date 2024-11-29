tablero = []
sudokuOK = False
for i in range(9):
    fila = input("fila " + str(i)+ ": ")
    if not fila.isnumeric():
        print("El numero introducido no es valido")
        break
    elif sorted(fila) != list("123456789"):
        print (sorted(fila))
        print("la linea debe contener todos los digitos del intervalo 1-9")
        break
    else:
        sudokuOK = True
        tablero.append(fila)
        
        
if sudokuOK:
    print("tablero is ok ")
else:
    print("tablero no es valido")