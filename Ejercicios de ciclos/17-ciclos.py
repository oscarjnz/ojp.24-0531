#17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.
print('\n----------Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.----------')

while True:
    question = str(input('\nSe leerán números hasta que digites 0 y se determinará a cuánto es igual el promedio de los números terminados en 5. ¿Desea continuar? Si/No: ')).strip().lower()

    if question != 'si':
        print('Excelente, gracias.')
        break
    else: 
        suma = 0
        conteo = 0

        while True:
            print('\nSi desea terminar el proceso, marque el 0.')
            numero = int(input('Ingrese un número: '))

            if numero == 0:
                break
            if numero % 10 == 5:
                suma += numero
                conteo += 1
        if conteo == 0:
            print('--*Lo sentimos. No se ingresaron números terminados en 0.*--')
        else:
            promedio = suma/conteo
            print('El promedio de los números que terminan en 5 es: ',promedio)
    break