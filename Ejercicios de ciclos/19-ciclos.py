#19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.
print('\n----------Leer un número entero y mostrar en pantalla su tabla de multiplicar.----------')

while True:
    numero = int(input('\nIngrese un número: '))

    if numero <= 0:
        print('\n--*Ingrese un valor mayor a 0.*--')
    else:
        print('\nLa tabla de multiplicar de hasta el 12 del',numero,'es: ')
        for i in range(1, 12+1):
            prod = numero * i
            print(numero,'x',i,'=',prod)
        break