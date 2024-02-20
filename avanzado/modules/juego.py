import os
import modules.menu as m
import modules.validate as v
def AddJuego(categorias:dict):
    os.system('cls')
    print('seleccione a que categoria desea agregar el juego')
    os.system('pause')
    op = m.MenuCat()
    if (op == 1):
        cat = categorias.get('novatos')['jugadores']
        aux = categorias.get('novatos')['juegos']
    elif (op == 2):
        cat = categorias.get('intermedio')['jugadores']
        aux = categorias.get('intermedio')['juegos']
    elif(op == 3):
        cat = categorias.get('avanzado')['jugadores']
        aux = categorias.get('avanzado')['juegos']
    if (len(cat)>=5):  
        nro = str(len(aux)+1).zfill(3)
        print('Ingrese el primer jugador')
        j1 = v.ValidateName(cat)
        print('Ingrese el segundo jugador')
        j2 = v.ValidateName(cat)
        print(f'Ingerse la cantidad de puntos hechos por el jugador {j1}')
        pt1 = v.ValidateInt()
        print(f'Ingerse la cantidad de puntos hechos por el jugador {j2}')
        pt2 = v.ValidateInt()
        for key,values in cat.items():
            if (j1 in values['nombre']):
                k1 = key
            elif (j2 in values['nombre']):
                k2 = key
        if (pt1>pt2):
            winner = j1
            loser = j2
            pa = pt1 - pt2
            cat[k1]['PJ'] += 1
            cat[k1]['PG'] += 1
            cat[k1]['PA'] += pa
            cat[k1]['TP'] += 2
            cat[k2]['PJ'] += 1
            cat[k2]['PP'] += 1
        elif(pt2>pt1):
            winner = j2
            loser = j1
            pa = pt2 - pt1
            cat[k2]['PJ'] += 1
            cat[k2]['PG'] += 1
            cat[k2]['PA'] += pa
            cat[k2]['TP'] += 2
            cat[k1]['PJ'] += 1
            cat[k1]['PP'] += 1
        else:
            winner = 'N/A'
            loser = 'N/A'
            cat[k2]['PJ'] += 1
            cat[k1]['PJ'] += 1
        nWDate = {
            'Jugador1':j1,
            'Jugador2':j2,
            'Puntos J1':pt1,
            'Puntos J2':pt2,
            'Ganador': winner,
            'Perdedor':loser
        }
        aux.update({nro:nWDate})
    else:
        os.system('cls')
        print('la categoria debe contar con minimo 5 jugadores para poder registrar juegos')
        os.system('pause')