#Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.
print('\nLeer 10 números enteros y determinar en qué posición está el número primo con más dígitos pares.\n')

numeros = []

for i in range(10):
    numero = int(input(f'Ingrese el número {i+1}: '))
    numeros.append(numero)

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

max_digitos_pares = -1
posicion = -1

for i in range(10):
    numero = numeros[i]
    if es_primo(numero):
        digitos_pares = 0
        for digito in str(numero):
            if int(digito) % 2 == 0:
                digitos_pares += 1
        if digitos_pares > max_digitos_pares:
            max_digitos_pares = digitos_pares
            posicion = i

if posicion != -1:
    print(f'\nEl número primo con más dígitos pares está en la posición: {posicion + 1}')
else:
    print('\nNo hay números primos en la lista.')
