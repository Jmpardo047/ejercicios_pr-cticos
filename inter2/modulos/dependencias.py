import os
def AddDepend(dependencias:dict):
    os.system('cls')
    nombre = input('Ingrese el nombre de la Dependencia que desea agregar:  ')
    nW = {
        'dependencia':nombre,
        'dispositivos':{},
        'transporte':{
            'carro':0,
            'transporte público':0,
            'moto':0,
            'otro':0
        },
        'consumo':0.0
    }
    id = str(len(dependencias)+1)
    if (len(dependencias)<=0):
        dependencias.update({id:nW})
        print(f'la dependencia {nombre} ha sido agregada con el id: {id}')
        os.system('pause')
    elif(validInfo(dependencias,nombre) == False):
        dependencias.update({id:nW})
        print(f'la dependencia {nombre} ha sido agregada con el id: {id}')
        os.system('pause')
    else:
        AddDepend(dependencias)  

def validInfo(dependencias:dict,nombre):
    for keys,values in dependencias.items():
        if (nombre in values['dependencia']):
            print('esta dependencia ya fue agregada')
            os.system('pause')
            return True
    return False
