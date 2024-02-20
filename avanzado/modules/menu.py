import os
def MainMenu():
    lstOp = (1,2,3,4)
    titulo = '''
    ********************
    * TORNEO PING PONG *
    ********************
    '''
    opciones = '1. Registrar Jugador\n2. Agregar Juego\n3. Ver registros\n4. salir'
    os.system('cls')
    try:
        print(titulo)
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MainMenu()
    except ValueError:
        return MainMenu()
    else:
        return n

def MenuCat():
    lstOp = (1,2,3)
    opciones = '1. Novatos\n2. Intermedio\n3. Avanzado'
    os.system('cls')
    try:
        print(opciones)
        x = int(input(')..'))
        if (x not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuCat()
    except ValueError:
        return MenuCat()
    else:
        return x
    
def MenuRegistro():
    lstOp = (1,2,3,4)
    opciones = '1. Ver tabla general por categoria\n2. ver estadísticas de jugador\n3. ver registro de partidos por categoria\n4. Salir'
    os.system('cls')
    try:
        print(opciones)
        x = int(input(')..'))
        if (x not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuRegistro()
    except ValueError:
        return MenuRegistro()
    else:
        return x