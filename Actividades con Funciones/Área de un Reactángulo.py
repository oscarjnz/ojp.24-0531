def largo():
    largo = float(input('\nIngrese el valor del largo del rectangulo: '))
    return largo
def ancho():
    ancho = float(input('Ingrese el valor del ancho del rectángulo: '))
    return ancho

def area(largo, ancho):
    area = largo * ancho
    return area

valor_largo = largo()
valor_ancho = ancho()
areaDelRectangulo = area(valor_largo, valor_ancho)

print(f'\nEl área del rectángulo es: {areaDelRectangulo}')