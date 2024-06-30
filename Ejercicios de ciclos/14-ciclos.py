#14. Mostrar en pantalla los primeros 20 múltiplos de 3.
print('\n----------14. Mostrar en pantalla los primeros 20 múltiplos de 3.----------')

while True:
    question = str(input('\nA continuación se mostrarán los primeros 20 multiplos de 3. ¿Desea continuar? Si/No: ')).strip().lower()

    if question != 'si':
        print('Gracias')
    else:
        print('Los primeros 20 multiplos de 3 son: ')
        for i in range(1,61): #<----'''61 para que llegue a 60 y sean 20 números'''
            if i % 3 == 0:
                print(i)
        break