import json as j
import tkinter as tk
import requests as r
from datetime import datetime as dt
import matplotlib.pyplot as plt


'''
El proyecto "Conversor de Monedas" tiene como objetivo proporcionar una herramienta eficiente y fácil de usar
para convertir valores entre 5 diferentes monedas utilizando tasas de cambio actualizadas.
Este conversor es útil para viajeros, negocios internacionales, y cualquier persona que
necesite realizar conversiones monetarias rápidas y precisas.
'''

print('\n***************CONVERSOR DE MONEDAS***************')
# Necesito definir el valor de cada cambio
cambio = {
    'EUR_USD': 1.08,  # EURO A DÓLAR
    'USD_EUR': 0.92,  # DÓLAR A EURO
    'DOP_USD': 0.017,  # PESO A DÓLAR
    'USD_DOP': 59.50,  # DÓLAR A PESO
    'DOP_EUR': 0.016,  # PESO A EURO
    'EUR_DOP': 64.21,  # EURO A PESO
    'GBP_DOP': 76.34,  # LIBRA A PESO
    'DOP_GBP': 0.013,  # PESO A LIBRA
    'USD_GBP': 0.78,  # DÓLAR A LIBRA
    'GBP_USD': 1.29,  # LIBRA A DÓLAR
    'GBP_EUR': 1.19,  # LIBRA A EURO
    'EUR_GBP': 0.84,  # EURO A LIBRA
    'JPY_USD': 0.0066,  # YEN A DÓLAR
    'USD_JPY': 152.41,  # DÓLAR A YEN
    'JPY_EUR': 0.0061,  # YEN A EURO
    'EUR_JPY': 166.98,  # EURO A YEN
    'JPY_DOP': 0.39,  # YEN A PESO
    'DOP_JPY': 2.59  # PESO A YEN
}

# Debo guardar el historial de las conversiones
historial = []

def cargar_historial():
    try:
        with open('historial.json', 'r') as file:
            return j.load(file)
    except FileNotFoundError:
        return []

# Ahora, necesito guardar dicho archivo
def guardar_historial(historial):
    with open('historial.json', 'w') as file:
        j.dump(historial, file)

# Después, simulamos el obtener las tasas de cambio
def obtener_tasas(origen, destino):
    key = f'{origen}_{destino}'
    return cambio.get(key, None)

# Esta es la parte más importante. Convertiremos la moneda
def convert(cantidad, origen, destino):
    tasa_cambio = obtener_tasas(origen, destino)
    if tasa_cambio:
        return cantidad * tasa_cambio
    else:
        print('Lo sentimos. No podemos realizar esta conversión')
        return None

# Guardar la conversión en el historial
def reg_conversión(cantidad, origen, destino, tasa_cambio, resultado):
    conversion = {
        'fecha': dt.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cantidad': cantidad,
        'origen': origen,
        'destino': destino,
        'tasa de cambio': tasa_cambio,
        'resultado': resultado
    }
    historial.append(conversion)
    guardar_historial(historial)

# Mostramos el historial de conversiones
def mostrar_historial():
    for conversion in historial:
        print(conversion)

# Generamos la simulación de un gráfico
def grafico():
    fechas = [f'2024-07-{i}' for i in range(1, 10)]
    valores = [0.58 + i*0.01 for i in range(9)]
    plt.plot(fechas, valores)
    plt.xlabel('Fecha')
    plt.ylabel('Tasa de cambio USD-DOP')
    plt.title('Historial de Tasas de Cambio USD-DOP')
    plt.show()

# Aquí, iniciamos el programa principal
historial = cargar_historial()

while True:
    print('\n***MENÚ PRINCIPAL***: CONVERTIR - HISTORIAL - GRÁFICO - SALIR')
    opcion = input('Elija una opción: ').lower()

    if opcion == 'salir':
        break
    elif opcion == 'convertir':
        cantidad = float(input('\nIngrese la cantidad que desea convertir: '))
        origen = input('Ingrese la moneda de origen (USD, EUR, JPY, GBP, DOP): ').upper()
        destino = input('Ingrese la moneda de destino (USD, EUR, JPY, GBP, DOP): ').upper()
        resultado = convert(cantidad, origen, destino)
        if resultado:
            tasa_cambio = obtener_tasas(origen, destino)
            reg_conversión(cantidad, origen, destino, tasa_cambio, resultado)
            print(f'\nResultado: {resultado} {destino}')
    elif opcion == 'historial':
        mostrar_historial()
    elif opcion == 'grafico':
        grafico()
    else:
        print('\n*********************ESTA OPCIÓN NO ES VÁLIDA*********************')







'''
                                                                     Funcionalidades Principales

    #Conversión de Monedas:
Permite convertir cantidades entre una gran variedad de monedas utilizando tasas de cambio actualizadas.
Los usuarios pueden ingresar la cantidad, la moneda de origen y la moneda de destino para obtener el valor convertido.

    #Historial de Conversiones:
Almacena y muestra un registro de todas las conversiones realizadas, incluyendo la fecha, hora, cantidad, monedas de origen y destino, tasa de cambio utilizada y el resultado de la conversión.
Permite a los usuarios revisar sus conversiones pasadas para referencia futura.

    #Gráfico de Historial de Tasas de Cambio:
Genera un gráfico visual del historial de tasas de cambio para una moneda específica (ejemplo: USD-DOP), mostrando cómo ha variado la tasa de cambio a lo largo del tiempo.
Ayuda a los usuarios a visualizar tendencias y tomar decisiones informadas basadas en datos históricos.


    #Visualización de Tasas de Cambio:
Muestra una lista de las tasas de cambio actuales con relación al dólar estadounidense (USD) para todas las monedas disponibles.
Permite a los usuarios conocer las tasas de cambio sin necesidad de realizar una conversión.
'''