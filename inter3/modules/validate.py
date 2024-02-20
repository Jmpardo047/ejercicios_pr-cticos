import os

def ValidateInt()->int:
    try:
        x = int(input(')..'))
    except ValueError:
        print('El valor ingresado no es correcto')
        os.system('pause')
        return ValidateInt()
    else:
        return x

def ValidateFloat()->float:
    try:
        x = float(input(')..'))
    except ValueError:
        print('El valor ingresado no es correcto')
        os.system('pause')
        return ValidateFloat()
    else:
        return x