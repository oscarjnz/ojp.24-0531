#4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.

print('\n-------------------------Leer dos números y mostrar todos los enteros comprendidos entre ellos.---------------------')
while True:
    n1 = int(input('\nIngrese el 1er número: '))
    n2 = int(input('Ingrese el 2do número: '))

    if n1 < 0 or n2 < 0:
        print('\nSolo números positivos.')
    elif n1 == n2:
        print('\nColoca valores distintos.')
    elif n1 > n2:
        print('\nNo califica. Coloca los números en orden ascendente.')
    else:
        print('\nLos valores comprendidos entre',n1,'y',n2,'son:')
        for i in range(n1, n2+1):
            print(i)
        break