#1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.

print('\n-----------------------*-----------------------')

while True:
    numero = int(input('\nIngrese un número: '))

    if numero < 0:
            print('Trabajamos con números positivos.')
    elif numero == 0:
            print('Al', numero,'le preceden todos los números negativos.')
    elif numero == 1:
            print('El',numero,'está entre 0 y ese mismo número.')
    else:
        print('Los números comprendidos entre 1 y',numero,'son: ')
        for i in range(1, numero + 1):
            print(i)

    break



'''
Querido maestro, le pongo el 0 a los siguientes 
ejercicios para que se vea un poco mejor, 
teniendo en cuenta que el cero, aunque sea 
ausencia de cantidad, también es un número y 
debe ser tomado en cuenta. Espero pueda comprenderme.
'''