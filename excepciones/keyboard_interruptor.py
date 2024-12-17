 
string = 'lokisimo'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracios!')