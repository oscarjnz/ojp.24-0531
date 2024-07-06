#5) Retornar la cantidad de veces que se repite el último caracter
print('\n', '-'*10, 'Retornar la cantidad de veces que se repite el último caracter', '-'*10)

while True:
    print('\n**Soy El Mejor Programador de la Historia.**')
    texto = '\n**Soy El Mejor Programador de la Historia**'
    question = input('\nSe mostrarán la cantidad de veces que se repite el último caracter del texto de arriba. ¿Desea continuar? Si/No: ').strip().lower()

    if question != 'si':
        print('Muchas gracias.')
        break
    else:
        print(texto.count('a'))