#10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.
print('\n----------Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.----------')
while True:
    numero = int(input('\nIngrese un número: '))

    if numero == 0 or numero == 1:
        print('--*Debe ser mayor que 1.*--')
    elif numero < 0:
        print('--*Debe ser solo positivo.*--')
    else:
        suma = 0
        for i in range(1, numero + 1):
            suma += i
        print('\nLa suma desde 1 hasta',numero,'es:',suma)
        break

