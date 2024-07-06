#4) Retornar los dos últimos caracteres del texto
print('\n', '-'*10, 'Retornar los dos últimos caracteres del texto', '-'*10)

while True:
    print('\n**Soy El Mejor Programador de la Historia.**')
    texto = '\n**Soy El Mejor Programador de la Historia**'
    question = input('\nSe mostrarán los dos últimos caracteres del texto de arriba. ¿Desea continuar? Si/No: ').strip().lower()

    if question != 'si':
        print('Muchas gracias.')
        break
    else:
        print(texto[40:45])
