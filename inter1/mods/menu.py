import os
def MainMenu():
    lstOpciones = [1,2,3,4,5]
    titulo = '''
   ********************************** 
   * REGISTRO DE SISMOS EN COLOMBIA *
   ********************************** 
'''
    opciones = '1. Registrar ciudad\n2. Registrar sismo\n3. Buscar sismo por ciudad\n4. Informe de riesgo\n5 Salir'
    os.system('cls')
    try:
        print(titulo)
        print(opciones)
        n=int(input(')..'))
        if (n not in lstOpciones):
            return MainMenu()
    except ValueError:
        print('El valor ingresado es inválido')
        os.system('pause')
        return MainMenu()
    else:

        return n