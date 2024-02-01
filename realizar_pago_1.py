# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:22:01 2024

@author: USUARIO
"""

def realizar_pago():
    """
    Calcula el total y el precio promedio de una serie de artículos dados.

    Calcula el total, el número total de elementos y el precio promedio por artículo.
    También maneja números negativos y evita la división por cero.

    Returns:
    None
    """
    total = 0
    recuento = 0
    más_artículos = True

    while más_artículos:
        precio = float(input('Ingrese el precio del artículo (0 para finalizar): '))

        if precio < 0:
            print('Error: No se permiten precios negativos. Intente nuevamente.')
        elif precio != 0:
            recuento += 1
            total += precio
            print('Subtotal: $', total)
        else:
            más_artículos = False

    if recuento > 0:
        promedio = total / recuento
        print('Total de elementos:', recuento)
        print('Total $', total)
        print('Precio promedio por artículo: $', promedio)
    else:
        print('No se ingresaron precios o se ingresaron solo ceros.')
        print('No se puede calcular el promedio sin datos.')

# Ejemplo de uso
realizar_pago()
