from mods import menu as m
from mods import ciudades as c
from mods import sismos as s
from mods import informe as i
if __name__=='__main__':
    ciudades = []
    isActive = True
    while isActive:
        m.os.system('cls')
        n = m.MainMenu()
        if (n == 1):
            c.AddCiudad(ciudades)
        elif (n == 2):
            s.AddSismo(ciudades)
        elif (n == 3):
            s.SrchSismo(ciudades)
        elif (n == 4):
            i.Promedios(ciudades)
        elif (n == 5):
            m.os.system('cls')
            print('Hasta pronto')
            m.os.system('pause')
            isActive = False