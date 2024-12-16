def mal_asunto(n):
    try:
     return n / 0
    except:
        print("pasó de  nuevo")
        raise ValueError
try:
    mal_asunto(0)
except ArithmeticError:
    print("Error")
    exit(0)
    

print("FIN")