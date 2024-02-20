import os
from modulos import validate as v
from modulos import menu as m
def RegConsumos(dependencias:dict):
    if (len(dependencias) !=  0):
        x = m.MenuConsumo()
        if (x == 1):
            AddDevice(dependencias)
        elif (x == 2):
            AddTransporte(dependencias)
    else:
        print('aun no ha agregado dependencias')
        os.system('pause')

def AddDevice(dependencias:dict):
    os.system('cls')
    print('Las emisiones se registrarán por cada dispositivo y su respectivo consumo en la dependencia')
    dep = input('Ingrese el id de la dependencia\n)..')
    if (dep in dependencias.keys()):
        dv = input('ingrese el nombre del dispositivo que quiere agregar\n)..')
        print('Ingrese el consumo del dispositivo en watts (W)')
        consumo = v.ValidateFloat()
        co2 = (((consumo*8)/1000)*24)*0.374
        dependencias[dep]['dispositivos'].update({dv:consumo})
        dependencias[dep]['consumo'] += co2   
        rep = bool(input('desea agregar otro dispositivo? S(si) o Enter(no):'))
        if (rep == True):
            AddDevice(dependencias)
        else:
            pass
    else:
        print('dependencia no encontrada')
        os.system('pause')
        AddDevice(dependencias)

def AddTransporte(dependencias:dict):
    os.system('cls')
    print('Las emisiones se registrarán segun el tipo de vehiculo que utilice y los kilometros recorridos')
    dep = input('Ingrese el id de la dependencia\n)..')
    if (dep in dependencias.keys()):
        x = m.MenuTransport()
        if (x == 1):
            fEmision = 121
            add = 'carro'
        elif (x == 2):
            fEmision = 49
            add = 'transporte público'
        elif (x == 3):
            fEmision = 53
            add = 'moto'
        elif (x == 4):
            fEmision = 17
            add = 'otro'
        print('Ingrese la cantidad de km que recorre usando el transporte')
        km = v.ValidateFloat()
        co2 = ((km*fEmision)*2)*24
        dependencias[dep]['consumo'] += co2
        dependencias[dep]['transporte'][add] += 1
        rep = bool(input('desea agregar otro transporte? S(si) o Enter(no):'))
        if (rep == True):
            AddTransporte(dependencias)
        else:
            pass
    else:
        print('dependencia no encontrada')
        os.system('pause')
        AddTransporte(dependencias) 
