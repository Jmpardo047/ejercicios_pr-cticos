import os
def Ganancias(productos:dict):
    os.system('cls')
    id = input('ingrese el id del producto: ')
    if (id in productos):
        pr = productos.get(id)
        compra = pr['valor compra']
        venta = pr['valor venta']
        stock = pr['stock']
        name = pr['producto']
        ganancia = (venta-compra)*stock
        print(f'La ganancia potencial del producto {name} es {ganancia}')
        os.system('pause')
    else:
        Ganancias(productos)