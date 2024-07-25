def nombre():
    nombre = input('\nIngrese su nombre para darle un saludo: ')
    return nombre
def saludo():
    saludo = ('\nHola ')
    return saludo

name = nombre()
sayHi = saludo()

print(f'\n{sayHi}{name}')