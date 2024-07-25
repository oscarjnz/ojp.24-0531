def palindromo(frase):
    frase_clean = frase.lower().replace(' ', '')
    return frase_clean == frase_clean[::-1]

def fullFrase():
    texto = input('\nIngrese una palabra o frase: ')
    if palindromo(texto):
        print(f'\n"{texto}" es un palíndromo.')
    else:
        print(f'\n"{texto}" no es un palíndromo')

fullFrase()