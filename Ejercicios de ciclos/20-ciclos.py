#20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.
print('\n----------Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.----------')

while True:
    numero = int(input('\nIngrese un número: '))
    
    if numero == 0:
        print('El valor no puede ser',numero)

    elif numero >= 0:
        suma = 0
        x = 1
        factorial = 1
        for i in range(1, numero + 1):
            factorial = 1
            for a in range(1, i + 1):
                factorial *= a
            suma += factorial
            print('El factorial de',i,'es',factorial)
        print('\nLa sumatoria de los factoriales desde 1 hasta',numero,'es:',suma)
        break
    else:
        print('Por favor, ingrese un número positivo.')