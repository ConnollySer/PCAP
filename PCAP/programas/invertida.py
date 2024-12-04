frase = input("Introduce una frase: ")
minus = (frase.lower().replace('',''))
invertida = minus
if invertida == minus[::-1] : 
     print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")
print(invertida)