while True:
    text1=input("introduce una plabara ").upper()
    if not  text1.isalpha():
        print("no es una palabra")
        break
    else:
        text2= input("introduce la 2º palabra: ").upper()
        if not text2.isalpha():
            print("no es una palabra ")
        break
        
        

    
l1 = sorted(text1)
l2 = sorted(text2)
if l1 == l2:
    print("las palabras son iguales")
else:
    print("Las palabras no son iguales")
       