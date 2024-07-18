#Leer 10 números enteros y calcular la factorial de cada uno.
print('\nLeer 10 números enteros y calcular la factorial de cada uno.\n')

numeros = []

for i in range(10):
    numero = int(input(f'Ingrese el número {i+1}: '))
    numeros.append(numero)

def factorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

factoriales = []
for numero in numeros:
    factoriales.append(factorial(numero))

print(f'Las factoriales de los números leídos son: {factoriales}')