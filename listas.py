num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
impares =  [num for num in num if num % 2 != 0]
print(impares)

names = ['Oscar', 'Lisette', 'Astrid', 'Albert', 'Enrique', 'Luis', 'Carlos']
filtro = [name for name in names if 'o' in name.lower()]
print(filtro)