#Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.

print('\nLeer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.\n')

lista = []

for i in range(10):
    numero = int(input(f'Ingrese el valor {i+1}: '))
    lista.append(numero)

mayor_num = max(lista)
mayor_posc = lista.index(mayor_num)

print('\nEl mayor número de la lista es:',mayor_num,'y está en la posición:',mayor_posc+1)