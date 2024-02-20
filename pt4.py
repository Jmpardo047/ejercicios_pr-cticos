from modulos import validaciones as v
if __name__=='__main__':
    n = 0 
    tNum = 0
    tPar = 0
    tImpar = 0
    sumPar = 0
    SumImpar = 0
    pPares = 0
    pImpares = 0
    menor10 = 0
    mayor100 = 0
    entreRango = 0
    isActive = True
    while isActive:
        v.os.system('cls')
        print('ingrese un numero entero positivo')
        n = v.ValidateInt()
        if (n>1):
            tNum += 1
            if (n%2 == 0):
                tPar +=1
                sumPar += n
            else:
                tImpar += 1
                SumImpar += n
            if(n<10):
                menor10 += 1
            elif(n>=20 and n<=50):
                entreRango += 1
            elif(n>100):
                mayor100 += 1
        else:
            v.os.system('cls')
            isActive = False
    pPares = sumPar/tPar
    pImpares = SumImpar/tImpar
    print(f'El total de numeros ingresados es {tNum}')
    print(f'El total de numeros pares ingresados es {tPar}')
    print(f'El promedio de numeros pares ingresados es {pPares}')
    print(f'El promedio de numeros impares ingresados es {pImpares}')
    print(f'{menor10} numeros son menores que 10')
    print(f'{mayor100} numeros son mayores que 100')
    print(f'{entreRango} numeros estan en 20 y 50')