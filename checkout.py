# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:28:20 2024

@author: USUARIO
"""

def checkout():
    total = 0
    count = 0
    more_items = True
    
    while more_items:
        try:
            price = float(input('Enter price of item (0 when done): '))
            
            if price < 0:
                print('Error: No se permiten precios negativos. Intente nuevamente.')
            elif price != 0:
                count += 1
                total += price
                print('Subtotal: $', total)
            else:
                more_items = False
                
        except ValueError:
            print('Error: Ingrese un número válido. Intente nuevamente.')

    if count > 0:
        average = total / count
        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)
    else:
        print('No se ingresaron precios válidos.')

# Ejemplo de uso
checkout()
