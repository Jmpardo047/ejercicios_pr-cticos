import os

def MainMenu()->int:
    lstOp = (1,2,3,4,5,6)
    titulo = '''
  ***************************  
  *  GESTIÓN DE INVENTARIOS *
  *************************** 
'''
    opciones = '1. Registrar producto\n2. Visualizar productos\n3. Actualizar stock\n4. Informe de productos críticos\n5. Ganancia Potencial\n6.salir'
    os.system('cls')
    try:
        print(titulo)
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            return MainMenu()
    except ValueError:
        ('Digito ingresado inválido')
        os.system('pause')
        return MainMenu()
    else:
        return n
    
def MenuUpdate()->int:
    lstOp = (1,2)
    print('1. Agregar stock\n2. Restar Stock')
    try:
        n = int(input(')..'))
        if (n not in lstOp):
            return MenuUpdate()
    except ValueError:
        ('Digito ingresado inválido')
        os.system('pause')
        return MenuUpdate()
    else:
        return n