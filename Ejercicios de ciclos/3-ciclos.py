#3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.

print('\n-------------------------Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.---------------------')

while True:
    numero = int(input('\nIngrese un número: '))

    if numero < 0:
        print('Solo aceptamos números positivos.')

    else:
        print('Los divisores exactos de',numero,'son: ')
        for i in range(1, numero + 1):
            if numero % i == 0:    
                print(i)
        break