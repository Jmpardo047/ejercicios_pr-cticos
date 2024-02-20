import os 
from modules import menu as m
from modules import validate as v
from tabulate import tabulate
def UptStock(productos:dict):
    os.system('cls')
    id = input('ingrese el id del producto: ')
    if (id in productos):
        op = m.MenuUpdate()
        if (op == 1):
            VerifyMax(productos,id)
        elif (op == 2):
            VerifyMin(productos,id)          
    else:
        UptStock(productos)

def VerifyMax(productos:dict,id)->int:
    os.system('cls')
    print('Ingrese la cantidad de stock que desea agregar')
    nwStock = v.ValidateInt()
    productos[id]['stock'] += nwStock
    stock = productos[id]['stock']
    max = productos[id]['stock maximo']
    if (stock > max or nwStock < 0 ):
        productos[id]['stock'] -= nwStock
        print(f'Este numero excede limites del stock, intente con otro')
        os.system('pause')
        return VerifyMax(productos,id)
    else:
        print(f'se han agregado {nwStock} unidades al producto de codigo {id}')
        os.system('pause')

def VerifyMin(productos:dict,id)->int:
    os.system('cls')
    print('Ingrese la cantidad de stock que desea restar')
    nwStock = v.ValidateInt()
    productos[id]['stock'] -= nwStock
    stock = productos[id]['stock']
    min = productos[id]['stock minimo']
    if (nwStock < 0 ):
        productos[id]['stock'] += nwStock
        print(f'Este numero excede limites del stock, intente con otro')
        os.system('pause')
        return VerifyMin(productos,id)
    else:
        print(f'se han restado {nwStock} unidades al producto de codigo {id}')
        os.system('pause')

def CriticStock(productos:dict):
    os.system('cls')
    danger = []
    for keys,values in productos.items():
        if(values['stock']<values['stock minimo']):
            danger.append({'producto':values['producto'],'stock actual':values['stock'],'stock requerido':values['stock minimo']})
    print('estos son los productos que se encuentras por debajo del stock minimo')
    print(tabulate(danger,headers="keys",tablefmt="grid"))
    os.system('pause')