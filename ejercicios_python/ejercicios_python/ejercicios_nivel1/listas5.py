import string
alfa = string.ascii_lowercase;
multiplos = []
for alf in alfa:
    if alfa.index(alf) % 3 == 0:
        multiplos.append(alf)
        
print(multiplos);