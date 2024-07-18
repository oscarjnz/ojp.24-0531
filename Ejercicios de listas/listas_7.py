#Leer 10 números enteros y calcular el promedio entero.
print('\nLeer 10 números enteros y calcular el promedio entero.\n')

numeros = []

for i in range(10):
    numero = int(input(f'Ingrese el número {i+1}: '))
    numeros.append(numero)

promedio = sum(numeros) // len(numeros)

print(f'\nEl promedio entero es: {promedio}')
