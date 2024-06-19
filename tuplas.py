print('\n-------------------------------TE MOSTRAMOS TU PROMEDIO!!!----------------------------------------')
print('Danos tus calificaciones y te daremos un promedio.')

nombre = input('\n***Permítenos tu nombre, por favor: ')
nota1 = int(input('\nIngresa la primera calificación: '))
nota2 = int(input('\nIngresa la segunda calificación: '))
nota3 = int(input('\nIngresa la tercera calificación: '))
nota4 = int(input('\nIngresa la cuarta calificación: '))
nota5 = int(input('\nIngresa la quinta calificación: '))
nota6 = int(input('\nIngresa la última calificación: '))

notas = [nota1, nota2, nota3, nota4, nota5, nota6]
promedio = sum(notas)/len(notas)

print('\nHemos calculado tu promedio', nombre,', es de', promedio)
if promedio >= 87: 
    print("\nMuchas felicidades", nombre,', tu promedio es excelente.')
elif 79 <= promedio <= 86:
    print("\nMuy bien", nombre,', pero puede ser mejor.')
else:
    print('\nLo sentimos', nombre, ',' 'debes mejorar tus calificaciones.')