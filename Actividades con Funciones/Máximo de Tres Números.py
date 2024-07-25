def maximo(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    elif num1 == num2 == num3:
        return print('Todos los valores son iguales.')
    else:
        return print('Lo sentimos, no podemos processar su solicitud.')
    
def determ():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    max_num = maximo(num1, num2, num3)
    print(f'\nEl número más grande entre {num1}, {num2} y {num3} es el {max_num}')

determ()