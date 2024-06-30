#13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
print('\n----------Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.----------')

while True:
    numero = int(input('\nIngrese un número: '))

    if numero <= 0:
        print('--*El valor debe ser positivo.*--')
    elif numero <= 4:
        print('--*Este valor no tiene multiplo de 5.*--')
    else:
        print('\nLos multiplos de 5 comprendidos entre 1 y',numero,'son: ')
        for i in range(1, numero + 1):
            if i % 5 == 0:
                print(i)
        break