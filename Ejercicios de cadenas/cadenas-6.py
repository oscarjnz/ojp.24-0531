#6) Retornar el texto invertido
print('\n', '-'*10, 'Retornar el texto invertido', '-'*10)

while True:
    print('\n**Soy El Mejor Programador de la Historia.**')
    texto = '\n**Soy El Mejor Programador de la Historia.**'
    question = input('Se mostrará el texto de arriba invertido. ¿Desea continuar? Si/No: ').strip().lower()

    if question != 'si':
        print('Muchas gracias.')
        break
    else:
        print(texto[::-1])