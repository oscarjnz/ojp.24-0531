def cap_datos():
    estudiantes = []

print('\n-------------------------------PROMEDIO----------------------------------------')
print('Danos tus calificaciones y te daremos tu promedio.')

while True:

    nombre = input('\n***Nombre: ')
    matricula = input('***Matricula: ')
    estudiante = [nombre, matricula]
    print('\nGracias,',nombre, '--',matricula,'--')

    nota1 = int(input('\nIngresa la primera calificación: '))
    nota2 = int(input('Ingresa la segunda calificación: '))
    nota3 = int(input('Ingresa la tercera calificación: '))
    nota4 = int(input('Ingresa la cuarta calificación: '))

    if nota1 <0:
        print('\nEl valor es negativo, intente de nuevo')
        nota1 = int(input('\nIngresa la primera calificación: '))
    if nota3 <0:
        print('\nEl valor es negativo, intente de nuevo')
        nota3 = int(input('\nIngresa la primera calificación: '))
    if nota4 <0:
        print('\nEl valor es negativo, intente de nuevo')
        nota4 = int(input('\nIngresa la primera calificación: '))
    if nota2 <0:
        print('\nEl valor es negativo, intente de nuevo')
        nota2 = int(input('\nIngresa la primera calificación: '))

    notas = [nota1, nota2, nota3, nota4]
    promedio = sum(notas)/len(notas)

    print('\nHemos calculado tu promedio', nombre,', es de',promedio)


    if promedio >= 87: 
        print("\nMUCHAS FELICIDADES", nombre,', tu promedio es excelente.')
    elif 79 <= promedio <= 86:
        print("\nMuy bien", nombre,', pero puede ser mejor.')
    else:
        print('\nLo sentimos', nombre, ',' 'debes mejorar tus calificaciones.')

    continuar = input("\n¿Deseas capturar otro estudiante? (si/no): ").strip().lower()
    if continuar != 'si':
        break