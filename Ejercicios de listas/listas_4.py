#Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo
print('\nLeer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo.\n')

while True:
    lista = []

    for i in range(10):
        numero = int(input(f'Ingrese el valor {i+1}: '))
        lista.append(numero)

    primos = ['2', '3', '5', '7']
    contador = 0

    for numero in lista:
        primer_digito = str(abs(numero))[0]
        if primer_digito in primos:
            contador += 1
    print(f'\nLa cantidad de números que comienzan con un dígito primo es: {contador}\n')