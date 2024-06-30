#11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.
print('\n----------Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.----------')

while True:
    numero = int(input('\nIngrese un número de 2 dígitos: '))

    if numero < 0 or numero > 99:
        print('\n--*DEBE TENER 2 DÍGITOS Y SER POSITIVO.*--')
    else:
        digito1 = numero // 10
        digito2 = numero % 10
        
        if digito1 == digito2:
            print('\n--*LOS DÍGITOS DEBEN SER DIFERENTES.*--')
        else:
            print('\nLos números comprendidos entre', digito1, 'y', digito2, 'son:')
            if digito1 < digito2:
                for i in range(digito1 + 1, digito2):
                    print(i)
            else:
                for i in range(digito2 + 1, digito1):
                    print(i)
        break
