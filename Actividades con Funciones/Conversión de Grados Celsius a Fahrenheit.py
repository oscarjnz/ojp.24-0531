def c_f(celcius):
    return (celcius * 9/5) + 32

def convrt():
    celcius = float(input('\nIngrese la temperatura (C): '))
    fahrenheit = c_f(celcius)
    print(f'\nLa temperatura de {celcius} grados Celcius equivale a {fahrenheit} grados Fahrenheit.')

convrt()