#Leer dos números enteros y si la diferencia entre los dos números es par mostrar en
#pantalla la suma de los dígitos de los números, si dicha diferencia es un número primo
#menor que 10 entonces mostrar en pantalla el producto de los dos números y si la diferencia
#entre ellos terminar en 4 mostrar en pantalla todos los dígitos por separado.

def n_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

#---------------Calcular la resta------------------
diferencia = abs(a - b)



#--------------------Si la diferencia es par, mostrar la suma de los dígitos de los números----------------------
if diferencia % 2 == 0:
    suma_a = sum(int(digito) for digito in str(abs(a)))
    suma_b = sum(int(digito) for digito in str(abs(b)))
    total = suma_a + suma_b
    print(f"La diferencia es par. La suma de los dígitos de los números es: {total}")



#-------------------Si la diferencia es un número primo menor que 10, mostrar el producto de los dos números----------------------------
elif n_primo(diferencia) and diferencia < 10:
    producto = a * b
    print(f"La diferencia es un número primo menor que 10. El producto de los dos números es: {producto}")



#--------------------Si la diferencia termina en 4, mostrar todos los dígitos por separado-------------------------------------
elif str(diferencia).endswith('4'):
    digito1 = [int(digito) for digito in str(abs(a))]
    digito2 = [int(digito) for digito in str(abs(b))]
    print(f"La diferencia termina en 4. Los dígitos por separado de los números son:")
    print(f"Dígitos del primer número: {digito1}")
    print(f"Dígitos del segundo número: {digito2}")



#---------------Si ningúno cumple, impreimir esto: ---------------------------
else:
    print("La diferencia no cumple ninguna de las condiciones especificadas.")
