#2) Retornar todo el texto en minusculas
print('\n','-'*10,'Retornar todo el texto en minusculas','-'*10)

while True:
    print('\n**Soy El Mejor Programador de la Historia.**')
    texto = '---Soy El Mejor Programador de la Historia.'.lower()
    question = input('\nEl texto de arriba se mostrará en minusculas. ¿Desea continuar? Si/No: ').strip().lower()

    if question != 'si':
        print('Muchas gracias.')
        break
    else:
        print(texto)