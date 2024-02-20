import os
def ValidateFloat():
    try:
        n=float(input(')..'))
    except ValueError:
        print('El valor ingresado no es correcto')
        os.system('pause')
        return ValidateFloat()
    else:
        return n
