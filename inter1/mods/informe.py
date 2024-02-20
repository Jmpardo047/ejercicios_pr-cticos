import os
from tabulate import tabulate
def Promedios(ciudades:list):
    totalSismo = len(ciudades[0]) - 1
    valid = validateAm(ciudades)
    if (valid == True):
        for item in ciudades:
            counter = 0
            for i,list in enumerate(item):
                if (i == 0):
                    pass
                else:
                    counter += item[i]
            promedio = counter/totalSismo
            print(f'el promedio de sismos en la ciudad {item[0]} es {promedio}')
        os.system('pause')
    else:
        pass

def validateAm(ciudades:list):
    valid = True
    counter = 0
    for item in ciudades:
        c1 = item
        for i,item2 in enumerate(ciudades):
            if (i == counter):
                pass
            else:
                c2 = ciudades[i]
                if (len(c1) != len(c2)):
                    print('Todas las ciudades deben tener la misma cantidad de sismos')
                    print(tabulate(ciudades))
                    os.system('pause')
                    valid = False
                    break
                else:
                    pass
        counter += 1
        if (valid == False):
            break
        else:
            pass
    return valid