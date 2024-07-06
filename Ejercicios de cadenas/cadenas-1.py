#1) Retornar todo el texto en mayúsculas
print('\n','-'*10,'Retornar todo el texto en mayusculas','-'*10)

while True:
    print('\n**Soy El Mejor Programador de la Historia.**')
    texto = '---Soy El Mejor Programador de la Historia.'.upper()
    question = input('\nEl texto de arriba se mostrará en mayusculas. ¿Desea continuar? Si/No: ').strip().lower()

    if question != 'si':
        print('Muchas gracias.')
        break
    else:
        print(texto)
        