import random
# Iteración sobre la lista de nombres que imprima solamente los nombres que tengan igual o más de tres vocales.
nombres = []
print("Por favor, ingrese 3 nombres: ")
for i in range(3):
    nombre = input(f"Ingresa el nombre {i+1}: ")
    nombres.append(nombre)

# Buscar las vocales en cada nombre
vocales = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")

for nombre in nombres:
    cont_vocales = 0
    for letra in nombre:
        if letra in vocales:
            cont_vocales += 1
    if cont_vocales >= 3:
        print(nombre)
    else:
        cont_vocales < 3
        print("El nombre colocado en esta linea tiene menos de 3 vocales.")