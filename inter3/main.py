from modules import menu as m
from modules import productos as p
from modules import update as up
import modules.ganancias as g
if __name__ == '__main__':
    productos = {}
    isActive = True
    while isActive:
        n = m.MainMenu()
        if (n == 1):
           p.AddProduct(productos)
        elif (n == 2):
            p.ViewProducts(productos)
        elif (n == 3):
            up.UptStock(productos)
        elif (n == 4):
            up.CriticStock(productos)
        elif (n == 5):
            g.Ganancias(productos)
        elif (n == 6):
            ('hasta pronto')
            m.os.system('pause')
            isActive = False