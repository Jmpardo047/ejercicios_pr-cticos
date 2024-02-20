import modules.menu as m
import modules.jugadores as j
import modules.registros as r
import modules.juego as jreg
if __name__ =='__main__':
    categorias={
        'novatos':{
            'jugadores':{},
            'juegos':{}
        },
        'intermedio':{
            'jugadores':{},
            'juegos':{} 
        },
        'avanzado':{
            'jugadores':{},
            'juegos':{}
        }
    }
    isActive = True
    while isActive:
        n = m.MainMenu()
        if (n == 1):
            j.AddPlayer(categorias)
        elif (n == 2):
            jreg.AddJuego(categorias)
        elif (n == 3):
            r.Registros(categorias)
        elif (n == 4):
            m.os.system('cls')
            print('Hasta luego')
            m.os.system('pause')
            isActive = False
   