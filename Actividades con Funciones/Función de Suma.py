def valor1():
    valor1 = float(input('\nIngrese el primer valor: '))
    return valor1
def valor2():
    valor2 =float(input('Ingrese el segundo valor: '))
    return valor2
def resultado(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

valor_1 = valor1()
valor_2 = valor2()
total = resultado(valor_1, valor_2)

print(f'\nLa suma de los dígitos ingresados es: {total}')