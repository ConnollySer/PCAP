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
        