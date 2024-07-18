#Leer 10 números enteros y determinar las posiciones de los que tienen más de 3 dígitos.
print('\nLeer 10 números enteros y determinar las posiciones de los que tienen más de 3 dígitos.\n')

numeros = []

for i in range(10):
    numero = int(input(f'Ingrese el número {i+1}: '))
    numeros.append(numero)

posiciones = []

for i in range(10):
    numero = numeros[i]
    if len(str(abs(numero))) >= 3:
        posiciones.append(i + 1)

print(f'\nLas posiciones de números con más de 3 dígitos son: {posiciones}')