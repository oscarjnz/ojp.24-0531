#2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

print('\n-------------------------Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.---------------------')

while True:
    numero = int(input('\nIngrese un número: '))
    
    if numero <= 0:
        print('Este número no es válido.')    
    else:
        print('Los pares comprendidos entre 0 y',numero,'son: ')
        for i in range(0, numero + 1):
            if i % 2 == 0:
                print(i)
        break