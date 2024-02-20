from mods import validate as v
from tabulate import tabulate
def AddSismo(ciudades:list):
    IsExist = True
    while IsExist:
        v.os.system('cls')
        cityName = input('Ingrese el nombre de la ciudad donde va a registar el sismo\n)..').upper()
        for item in ciudades:
            if (cityName in item):
                v.os.system('cls')
                print('Registre la magnitud del sismo')
                sismo = v.ValidateFloat()
                item.append(sismo)
                IsExist = False

def SrchSismo(ciudades:list):
    IsExist = True
    while IsExist:
        v.os.system('cls')
        cityName = input('Ingrese el nombre de la ciudad para ver su registro de sismos\n)..').upper()
        for item in ciudades:
            if (cityName in item):
                print('Ciudad----Sismos registrados')
                print(item)
                v.os.system('pause')
                IsExist = False
                break
                