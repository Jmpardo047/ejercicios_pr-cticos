import os
from tabulate import tabulate
def ResultComp(dependencias:dict):
    try:
        os.system('cls')
        data = list(dependencias.values())
        data.sort(key=lambda item : item['consumo'],reverse=True)
        top = data[0]['dependencia']
        print(tabulate(data,headers="keys",tablefmt='grid'))
        print(f'la dependencia que mas CO2 produjo fue {top}')
        os.system('pause')
    except IndexError:
        print('aun no ha agregado dependencias')
        os.system('pause')

def ResultCo2(dependencias:dict):
    os.system('cls')
    data = list(dependencias.values())
    co = []
    for item in data:
        co.append({'dependencia':item['dependencia'],'consumo':item['consumo']})
    print(tabulate(co,headers="keys",tablefmt='grid'))
    os.system('pause')