#15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
print('\n----------Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.----------')

while True:
    question = str(input('\nA continuación se mostrará en pantalla el resultado de sumar los primeros 20 múltiplos de 3. ¿Desea continuar? Si/No: ')).strip().lower()

    if question != 'si':
        print('Gracias')
        break
    else:
        suma = 0
        for i in range(1, 61):
            if i % 3 == 0:
                suma += i
        print('El resultado de sumar los primeros 20 múltiplos de 3 es:',suma)