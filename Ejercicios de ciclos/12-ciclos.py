#12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.
print('\n----------Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.----------')

while True:
    numero = int(input('\nIngrese un número de 3 dígitos: '))

    if numero < 100 or numero > 999:
        print('--*El número debe tener 3 dígitos.*--')
        
    else:
        digito1 = numero // 100
        digito2 = (numero // 10) % 10
        digito3 = numero % 10
        
        if digito1 == 1 or digito2 == 1 or digito3 == 1:
            print('--*El número SI tiene el dígito 1.*--')
        else:
            print('--*Este número NO contiene el dígito 1.*--')
        break