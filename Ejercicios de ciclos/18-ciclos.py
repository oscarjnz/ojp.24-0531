#18. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.
print('\n----------Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.----------')

while True:
    question = str(input('\nSe generarán los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1. ¿Desea continuar? Si/No: ')).strip().lower()

    if question != 'si':
        print('Excelente, gracias.')
        break
    else: 
        print('\nAquí están: ')
        for i in range(10, 0, -1):
            print(i)
        break