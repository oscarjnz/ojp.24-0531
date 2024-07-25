def vocal(letra):
    return letra.lower() in 'aeiou'

def buscar():
    palabra = input('\nIngrese una palabra: ')
    conteo = 0

    for letra in palabra:
        if vocal(letra):
            conteo += 1
            print(f'La palabra contiene la vocal: "{letra}"')
    print(f'\nNúmero total de vocales en la palabra: {conteo}')

buscar()