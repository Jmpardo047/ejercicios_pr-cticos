from modulos import validaciones as v
from tabulate import tabulate

if __name__=='__main__':
    estudiante = []
    edad = 0
    peso = 0.0
    altura = 0.0
    imc = 0.0
    pNormal = 0
    pSobre = 0
    pOb1 = 0
    pOb2 = 0
    pOb3 = 0
    for i in range(1,21,1):
        v.os.system('cls')
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
            pNormal += 1
        elif ( imc>=25 and imc<=29.9):
            estado = 'Sobrepeso'
            pSobre += 1
        elif ( imc>=30 and imc<=34.9):
            estado = 'Obesidad 1'
            pOb1 += 1
        elif ( imc>=35 and imc<=39.9):
            estado = 'Obesidad 2'
            pOb2 += 1
        elif ( imc>=40):
            estado = 'Obesidad 3'
            pOb3 += 1
        estudiante.append([nombre,edad,peso,altura,imc,estado])
    print(tabulate(estudiante,headers=['nombre','edad','peso','altura','imc','estado'],tablefmt='grid'))
    print(f'{pNormal} estudiantes se encuentran en el peso ideal')
    print(f'{pSobre} estudiantes tienen sobrepeso')
    print(f'{pOb1} estudiantes tienen obesidad grado 1')
    print(f'{pOb2} estudiantes tienen obesidad grado 2')
    print(f'{pOb3} estudiantes tienen obesidad grado 3')