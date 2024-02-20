import os
import modules.menu as m
import modules.validate as v
def AddPlayer(categorias:dict):
    os.system('cls')
    print('Ingrese a que categoria desea agregar al jugador')
    op = m.MenuCat()
    if (op == 1):
        cat = categorias.get('novatos')['jugadores']
    elif (op == 2):
        cat = categorias.get('intermedio')['jugadores']
    elif(op == 3):
        cat = categorias.get('avanzado')['jugadores']
    name = v.ValidateReg(categorias,cat)
    edad = v.ValidateAge(categorias,op)
    id = str(len(cat)+1).zfill(3)
    jugador = {
        'nombre':name,
        'edad': edad,
        'PJ':0,
        'PG':0,
        'PP':0,
        'PA':0,
        'TP':0
    }
    cat.update({id:jugador})

