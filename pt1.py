#programa que lee 3 números enteros positivos e imprime La sumatoria de los tres números.
from modulos import validaciones as v
if __name__=='__main__':
    n1 = 0
    n2 = 0
    n3 = 0
    isRunning = True
    while isRunning:
        v.os.system('cls')
        print('Ingrese el primer numero entero positivo')
        n1 = v.ValidateInt()
        print('Ingrese el segundo numero entero positivo')
        n2 = v.ValidateInt()
        print('Ingrese el tercer numero entero positivo')
        n3 = v.ValidateInt()
        sum = n1 + n2 + n3
        if(n1>-1 and n2-1 and n3>-1):
            print(f'la suma de {n1}+{n2}+{n3} es {sum}')
            isRunning = False
        else:
            print('todos los numeros deben ser negativos, intentar de nuevo')
            v.os.system('pause')