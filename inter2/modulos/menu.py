import os
def MainMenu():
    lstOpciones = [1,2,3,4,5]
    titulo = '''
   ***************************************
   * CO2 EN INSTALACIONES DE LA ALCALDIA *
   *************************************** 
'''
    opciones = '1. Registrar Dependencia\n2. Registrar consumo por dependencia\n3. Ver CO2 producido\n4. Dependencia que produce mayor CO2\n5 Salir'
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
def MenuConsumo()->int:
    os.system('cls')
    lstOp = (1,2)
    op = ('1. Consumo por dispositivos electronicos\n2. Consumo por transporte')
    print('Seleccione el tipo de consumo que desea ingresar')
    try:
        print(op)
        x = int(input(')..'))
        if (x not in lstOp):
            return MenuConsumo()
    except ValueError:
            print('Digito ingresado inválido')
            return MenuConsumo()
    else:
        return x
def MenuTransport():
    os.system('cls')
    lstOp = (1,2,3,4)
    op = ('1. Automóvil\n2. Transporte público\n3. Moto\n4. Otro')
    print('Seleccione el tipo de transporte que utiliza')
    try:
        print(op)
        x = int(input(')..'))
        if (x not in lstOp):
            return MenuConsumo()
    except ValueError:
            print('Digito ingresado inválido')
            return MenuConsumo()
    else:
        return x