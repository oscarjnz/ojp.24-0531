#16. Promediar los x primeros múltiplos de 2 & determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.
print('\n----------Promediar los x primeros múltiplos de 2 & determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.----------')

while True:
    x = int(input('\nIngrese el valor de x (número de múltiplos de 2): '))
    y = int(input('Ingrese el valor de y (número de múltiplos de 5): '))

    if x <= 0 or y <= 0:
        print('\n--*Este valor no es válido. Por favor, ingrese otro mayor que 0.*--')
    else:
        sumaX = sum(i*2 for i in range(1, x + 1))
        promX = sumaX / x

        sumaY = sum(1*5 for i in range(1, y + 1))
        promY = sumaY / y

        print('\nEl promedio de los primeros',x,'múltiplos de 2 es: ',promX)
        print('El promedio de los primeros',y,'múltiplos de 5 es: ',promY)

        if promX > promY:
                print('\nLos promedios son',promX,'y',promY,'--- X es mayor al promedio.')
        else:
                print('\nLos resultados son',promX,'y',promY,'---X no es mayor al promedio.')
        break