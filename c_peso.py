#INDICE DE MASA CORPORAL
print('INDICE DE MASA CORPORAL - IMC')

peso = float(input("\nINGRESE SU PESO(kg): "))
print('Su peso es: ', peso)

altura = float(input('\nINGRESE SU ALTURA(m): '))
print('Su altura es: ', altura**2)

imc = peso % altura
print('\nSu índice de masa corporal es: ', imc)