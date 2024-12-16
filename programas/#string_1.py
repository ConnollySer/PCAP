#string_1.py

num =int ( input ('introduce un numero: '))


print('Nº Introducido:', num)
1
print()
#concadenar cadena

saludo = 'holaaaaaa, '
quien = 'pishaaaa'

saludo = saludo + quien
print(saludo)

#iterar a traves de la  cadena

print()

for c in saludo:
    print(c)
    
#long. de la cadena (en caracteres)

print(len(saludo))

print('a' in 'saludo')
print('at' not in 'saludo')