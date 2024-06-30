#6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.
print('\n-------------------Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.-------------------')

while True:
    numero = int(input('\nIngrese un número de 3 dígitos: '))

    if numero > 1 and numero < 100:
        print('\n**ERROR!** -- Necesito un número de 3 dígitos.')

    elif numero < 0:
        print('\nSolo valores pósitivos.')

    else:
        print('Los números comprendidos entre 1 y',numero,'son: ')
        for i in range(1, numero + 1):
            print(i)
        break
