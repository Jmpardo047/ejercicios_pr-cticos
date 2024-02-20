import os
def ValidateInt():
    try:
        n=int(input(')..'))
    except ValueError:
        print('El valor ingresado no es correcto')
        return ValidateInt()
    else:
        return n
    
def ValidateFloat():
    try:
        n=float(input(')..'))
    except ValueError:
        print('El valor ingresado no es correcto')
        return ValidateFloat()
    else:
        return n
