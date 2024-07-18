#Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído.

print('\nLeer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído.\n')

while True:
    lista = []

    for i in range(10):
        numero = int(input(f'Ingrese el valor {i+1}: '))
        lista.append(numero)

    mayor_num_par = None
    mayor_posc_par = -1

    for i in range(len(lista)):
        if lista [i] % 2 == 0:
            if mayor_num_par is None or lista[i] > mayor_num_par:
                mayor_num_par = lista[i]
                mayor_posc_par = i

    if mayor_num_par is not None:
        print('\nEl mayor número par de la lista es:',mayor_num_par,'y está en la posición:',mayor_posc_par + 1,'\n')
        break    
    else:
        print('\nLo sentimos, no ha ingresado ningun número par. No podemos proseguir con el programa. Por favor, intente de nuevo.','\n')
        