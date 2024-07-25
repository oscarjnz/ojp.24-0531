def numero():
    numero = int(input('\nIngrese un número: '))
    return numero

def numPar(numero):
    return numero % 2 == 0

def numImpar(numero):
    return numero % 2 != 0
    
num = numero()

if numPar(num):
    print(f'\nEl número {num} es par.')
elif numImpar(num):
    print(f'\nEl número {num} es impar.')