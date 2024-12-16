
try:  
    y = 1/ 0
except (ZeroDivisionError, ArithmeticError):
    print("Estas teniendo un error aritmético")
except: 
    print("Otro error")

print("FIN")
