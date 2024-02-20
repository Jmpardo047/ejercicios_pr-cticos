from modulos import menu as m
from modulos import dependencias as d
from modulos import consumos as c
from modulos import resultados as r
if __name__ =='__main__':
    dependencias = {
    }
    isActive = True
    while isActive:
        n = m.MainMenu()
        if (n == 1):
            d.AddDepend(dependencias)
        elif (n == 2):
            c.RegConsumos(dependencias)
        elif (n == 3):
            r.ResultCo2(dependencias)
        elif (n == 4):
            r.ResultComp(dependencias)
        elif (n == 5):
            m.os.system('cls')
            print('Hasta pronto')
            m.os.system('pause')
            isActive = False