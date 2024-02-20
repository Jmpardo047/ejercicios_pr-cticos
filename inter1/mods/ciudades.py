import os
def AddCiudad(ciudades:list):
    os.system('cls')
    ciudad = str(input("Ingrese la ciudad que quiere agregar\n )..")).upper()
    if (len(ciudades)<=0):
        ciudades.append([ciudad])
    elif ((validInfo(ciudades,ciudad) == False) and (len(ciudades)<5)):
        ciudades.append([ciudad])
    elif (len(ciudades)>=5):
        print('El cupo de ciudades ya esta lleno')
        os.system('pause')
    else:
        AddCiudad(ciudades)    
def validInfo(ciudades:list,ciudad):
    for item in ciudades:
        if (ciudad in item):
            print('Este equipo ya ha sido agregado')
            os.system('pause')
            return True
    return False