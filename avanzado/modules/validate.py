import os
import modules.menu as m
def ValidateInt()->int:
    try:
        x = int(input(')..'))
    except ValueError:
        print('El valor ingresado no es válido')
        os.system('pause')
        return ValidateInt()
    else:
        return x
    
def ValidateReg(categorias:dict,cat:dict):
    os.system('cls')
    isFound = False
    try:
        name = input('Ingrese el nombre del nuevo jugador: ')
        for keys,values in cat.items():
            if (name in values['nombre']):
                print('el jugador ya esta registrado, intente con otro nombre')
                os.system('pause')
                return ValidateReg(categorias,cat)
    except IndexError:
        return name
    else:
        return name

def ValidateAge(categorias:dict,op:int)->int:
    print('Ingrese la edad del jugador')
    edad = ValidateInt()
    if (op == 1):
        if (edad>=15 and edad<=16):
            return edad
        else:
            print('la edad para categoria de novatos es solo entre 15 y 16')
            os.system('pause')
            return ValidateAge(categorias,op)
    elif (op == 2):
        if (edad>=17 and edad<=20):
            return edad
        else:
            print('la edad para categoria intermedio es solo entre 17 y 20')
            os.system('pause')
            return ValidateAge(categorias,op)
    elif (op == 3):
        if (edad > 20):
            return edad
        else:
            print('la edad para categoria avanzada es solo para mayores de 20 años')
            os.system('pause')
            return ValidateAge(categorias,op)

def ValidateName(cat:dict):
    isFound = False
    name = input(')..')
    for keys,values in cat.items():
        if (name in values['nombre']):
            isFound = True
    if(isFound == False):    
        print('Jugador no encontrado')
        os.system('pause')
        return ValidateName(cat)
    else:
        return name