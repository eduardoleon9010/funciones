# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:12:57 2024

@author: USUARIO
"""
def realizar_pago():
    """
    Calcula el total y el precio promedio de una serie de artículos dados.

    Calcula el total, el número total de elementos y el precio promedio por artículo.

    Returns:
    None
    """
    total = 0
    recuento = 0
    más_artículos = True

    while más_artículos:
        precio = float(input('Ingrese el precio del artículo (0 cuando haya terminado): '))
        if precio != 0:
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
        print('No se ingresaron precios.')

# Ejemplo de uso
realizar_pago()

