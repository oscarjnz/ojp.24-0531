#Leer 10 números enteros y contar cuántos son divisores de un número dado.
print('\nLeer 10 números enteros y contar cuántos son divisores de un número dado.\n')

numeros = []

for i in range(10):
    numero = int(input(f'Ingrese el número {i+1}: '))
    numeros.append(numero)

divisor = int(input('\nIngrese un número divisor: '))

divisores_exactos = sum(1 for numero in numeros if numero % divisor == 0)

print(f'\nEl número {divisor} tiene {divisores_exactos} divisores exactos en la lista.')
