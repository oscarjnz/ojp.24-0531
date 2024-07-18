#Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.
print('\nLeer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.\n')

while True:
    lista = []

    for i in range(10):
        numero = int(input(f'Ingrese el valor {i+1}: '))
        lista.append(numero)

    mayor_num_impar = None
    mayor_posc_impar = -1

    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            if mayor_num_impar is None or lista[i] > mayor_num_impar:
                mayor_num_impar = lista[i]
                mayor_posc_impar = i

    if mayor_num_impar is not None:
        print('\nEl mayor número par de la lista es:',mayor_num_impar,'y está en la posición:',mayor_posc_impar + 1,'\n')
        break
    else:
        print('\nLo sentimos, no ha ingresado ningun número impar. No podemos proseguir con el programa. Por favor, intente de nuevo.','\n')