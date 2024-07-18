#Leer 10 números enteros y contar cuántos son negativos.
print('\nLeer 10 números enteros y contar cuántos son negativos.\n')

numeros = []

# Leer 10 números enteros
for i in range(10):
    numero = int(input(f'Ingrese el número {i+1}: '))
    numeros.append(numero)

# Contar los números negativos
negativos = sum(1 for numero in numeros if numero < 0)

print(f'\nLa cantidad de números negativos es: {negativos}')
