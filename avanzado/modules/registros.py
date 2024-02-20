import os
import modules.menu as m
from tabulate import tabulate
def Registros(categorias:dict):
    x = m.MenuRegistro()
    if (x == 1):
        TablaCat(categorias)
    elif (x == 2):
        StatPl(categorias)
    elif (x == 3):
        TablaJuegos(categorias)
    elif (x == 4):
        pass

def TablaCat(categorias:dict):
    os.system('cls')
    print('Seleccione que tabla de categoría desea ver')
    n = m.MenuCat()
    if (n == 1):
        os.system('cls')
        op = categorias['novatos']['jugadores'].values()
        print(tabulate(op,headers="keys",tablefmt="grid"))
        os.system('pause')
    elif (n == 2):
        os.system('cls')
        op = categorias['intermedio']['jugadores'].values()
        print(tabulate(op,headers="keys",tablefmt="grid"))
        os.system('pause')
    elif (n == 3):
        os.system('cls')
        op = categorias['avanzado']['jugadores'].values()
        print(tabulate(op,headers="keys",tablefmt="grid"))
        os.system('pause')

def StatPl(categorias:dict):
    os.system('cls')
    print('Seleccione a que categoria pertenece el jugador')
    n = m.MenuCat()
    if (n == 1):
        cat = categorias.get('novatos')['jugadores']
    elif (n == 2):
        cat = categorias.get('intermedio')['jugadores']
    elif(n == 3):
        cat = categorias.get('avanzado')['jugadores']
    jugador = [SrchPl(cat)]
    print(jugador)
    print(tabulate(jugador,headers=['Nombre','edad','PJ','PG','PP','PA','TP'],tablefmt="grid"))
    os.system('pause')

def SrchPl(cat:dict):
    isFound = False
    os.system('cls')
    name = input('ingrese el nombre del jugador que quiere buscar: ')
    for keys,values in cat.items():
        if (name in values['nombre']):
            jugador = list(cat[keys].values())
            isFound = True        
    if (isFound == False):
        print('Jugador no encontrado')
        os.system('pause')
        return SrchPl(cat)
    else:
        return jugador
    
def TablaJuegos(categorias:dict):
    os.system('cls')
    print('Seleccione la tabla de categoría donde desea ver los juegos')
    n = m.MenuCat()
    if (n == 1):
        os.system('cls')
        op = categorias['novatos']['juegos'].values()
        print(tabulate(op,headers="keys",tablefmt="grid"))
        os.system('pause')
    elif (n == 2):
        os.system('cls')
        op = categorias['intermedio']['juegos'].values()
        print(tabulate(op,headers="keys",tablefmt="grid"))
        os.system('pause')
    elif (n == 3):
        os.system('cls')
        op = categorias['avanzado']['juegos'].values()
        print(tabulate(op,headers="keys",tablefmt="grid"))
        os.system('pause')