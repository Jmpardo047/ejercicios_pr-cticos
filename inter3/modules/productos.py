import os 
from modules import validate as v
from tabulate import tabulate
def AddProduct(productos:dict):
    os.system('cls')
    name = input('Ingrese el nombre del producto\n)..')
    print('Ingrese el valor de compra del producto')
    valueCom = v.ValidateFloat()
    print('Ingrese el valor de venta del producto')
    valueVen = v.ValidateFloat()
    print('Ingrese el stock mínimo del producto')
    stockMin = v.ValidateInt()
    print('Ingrese el stock máximo del producto')
    stockMax = v.ValidateInt()
    prov = input('Ingrese el nombre del proveedor del producto\n)..')
    nwP = {
        'producto':name,
        'valor compra':valueCom,
        'valor venta':valueVen,
        'stock minimo':stockMin,
        'stock maximo':stockMax,
        'stock': stockMin,
        'proveedor':prov
    }
    id = str(len(productos)+1).zfill(3)
    try:
        if (validInfo(productos,name) == False):
            productos.update({id:nwP})
            print(f'el producto {name} ha sido registrada con el id: {id}')
            os.system('pause')
        else:
            AddProduct(productos)
    except IndexError:
        productos.update({id:nwP})
        print(f'el producto {name} ha sido registrada con el id: {id}')
        os.system('pause')
    

def validInfo(productos:dict,name):
    for keys,values in productos.items():
        if (name in values['producto']):
            print('este producto ya fue agregado')
            os.system('pause')
            return True
    return False

def ViewProducts(productos:dict):
    os.system('cls')
    data = list(productos.values())
    print(tabulate(data,headers="keys",tablefmt="grid"))
    os.system('pause')
