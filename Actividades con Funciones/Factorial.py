def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
def numero():
    num = int(input('\nIngrese un número para calcular su factorial: '))
    if num < 0:
        print('***NO EXISTE ESTE FACTORIAL!***')
    else:
        resultado = factorial(num)
        print(f'\nEl factorial de {num} es {resultado}.')

numero()