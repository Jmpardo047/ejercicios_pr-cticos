from modulos import validaciones as v
from tabulate import tabulate
if __name__=='__main__':
    v.os.system('cls')
    estudiante = []
    edad = 0
    peso = 0.0
    altura = 0.0
    imc = 0.0
    nombre = input('Ingrese el nombre del estudiante: ')
    print('Ingrese la edad del estudiante')
    edad = v.ValidateInt()
    print('Ingrese el peso del estudiante')
    peso = v.ValidateFloat()
    print('Ingrese la esatura del estudiante')
    altura = v.ValidateFloat()
    imc = peso/(altura**2)
    if ( imc>=18.5 and imc<=24.9):
        estado = 'Normal'
    elif ( imc>=25 and imc<=29.9):
        estado = 'Sobrepeso'
    elif ( imc>=30 and imc<=34.9):
        estado = 'Obesidad 1'
    elif ( imc>=35 and imc<=39.9):
        estado = 'Obesidad 2'
    elif ( imc>=40):
        estado = 'Obesidad 3'
    estudiante.append([nombre,edad,peso,altura,imc,estado])
    print(tabulate(estudiante,headers=['nombre','edad','peso','altura','imc','estado'],tablefmt='grid'))