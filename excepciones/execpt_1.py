try:  
    y = 1/ 0
except ZeroDivisionError:
    print("Estas dividiendo entre cero")
except ArithmeticError:
    print("Problema  aritmetico")
except: 
    print("Otro error")
