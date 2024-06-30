#7. Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.
print('\n-------------------Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.-------------------')

while True:
    question = str(input('\nA continuacion, se mostrarán los números del 1 al 100. ¿Desea continuar?: ')).strip().lower()
    for i in range(1, 101):
        if question == 'si':
            print(i)

        elif question == 'no':
            print('\nGracias')
            break