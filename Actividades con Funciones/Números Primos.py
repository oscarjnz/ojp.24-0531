def primo(numero):
    if numero<= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    
def num_primo():
    numero = int(input('\nIngrese un número para saber si es primo: '))
    if primo(numero):
        print(f'\n{numero} es un número primo.\n')
    else:
        print(f'\n{numero} no es un número primo.\n')

num_primo()