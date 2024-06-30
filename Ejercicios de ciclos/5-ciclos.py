#5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.
print('\n-------------------Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.-------------------')

while True:
    n1 = int(input('\nIngrese el 1er número: '))
    n2 = int(input('Ingrese el 2do número: '))

    if n1 == n2:
        print('Los números deben ser distintos.')
    elif n1 > n2:
        print('No es válido. Debes colocarlos en orden ascendente.')
    else:
        print('Los números terminados en 4 entre',n1,'y',n2,'son: ')
        for i in range(n1, n2 + 1):
            if i % 10 == 4:
                print(i)
        break