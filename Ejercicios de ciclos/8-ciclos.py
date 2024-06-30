#8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.
print('\n------------------------Mostrar en pantalla todos los pares comprendidos entre 20 y 200.-----------------------')


while True:
    question = str(input('\n¿Desea ver los números pares del 20 al 200? - Si/No: ')).strip().lower()
    if question == 'si':
        for i in range(20, 200 + 1):
                if i % 2 == 0:
                    print (i)

    elif question == 'no':
        print('Gracias.')
        break