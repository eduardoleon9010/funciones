# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:33:43 2024

@author: USUARIO
"""

def suma_vectorial():
    """
    Suma dos vectores tridimensionales.

    Esta función solicita al usuario que ingrese las componentes de dos vectores tridimensionales
    y devuelve un nuevo vector que es la suma de los dos vectores recibidos.

    Returns:
        tuple: Un vector tridimensional resultado de la suma de los dos vectores recibidos,
        representado como una tupla de tres valores flotantes.
    """
    # Solicitar al usuario que ingrese las componentes del primer vector
    print("Ingrese las componentes del primer vector:")
    x1 = float(input("Componente x: "))
    y1 = float(input("Componente y: "))
    z1 = float(input("Componente z: "))

    # Solicitar al usuario que ingrese las componentes del segundo vector
    print("\nIngrese las componentes del segundo vector:")
    x2 = float(input("Componente x: "))
    y2 = float(input("Componente y: "))
    z2 = float(input("Componente z: "))

    # Sumar las componentes de los vectores
    suma_x = x1 + x2
    suma_y = y1 + y2
    suma_z = z1 + z2
    
    # Retornar el vector resultado como una tupla
    return (suma_x, suma_y, suma_z)

# Llamar a la función y mostrar el resultado
resultado = suma_vectorial()
print("\nEl resultado de la suma de los vectores es:", resultado)
