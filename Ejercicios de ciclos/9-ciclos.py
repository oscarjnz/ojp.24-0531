#9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.

print('\n------------------------Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.-----------------------')

while True:
    question = str(input('\n¿Desea ver los números terminados en 6 desde el 25 al 250? - Si/No: ')).strip().lower()
    if question == 'si':
        for i in range(25, 250 + 1):
                if i % 10 == 6:
                    print (i)

    elif question == 'no':
        print('Gracias.')
        break