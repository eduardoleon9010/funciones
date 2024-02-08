# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:09:01 2024

@author: USUARIO
"""

def aplicar_filtro(imagen: list, filtro: tuple) -> list:
    """
    Aplica un filtro a una imagen representada como una matriz de tuplas de valores RGB.

    Args:
    imagen (list): Matriz que representa la imagen, donde cada elemento es una tupla de 3 flotantes entre 0 y 1
                   representando los valores R, G y B del píxel.
    filtro (tuple): Tupla de tres booleanos, donde cada booleano indica si se debe conservar el valor del componente
                    correspondiente (R, G, B) de cada píxel. True conserva el componente, False lo elimina.

    Returns:
    list: Matriz que representa la imagen con el filtro aplicado.
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    nueva_imagen = []

    for i in range(alto):
        fila_nueva = []
        for j in range(ancho):
            r, g, b = imagen[i][j]
            temp = [r, g, b]
            for k in range(3):
                if not filtro[k]:
                    temp[k] = 0
            nuevo_pixel = tuple(temp)
            fila_nueva.append(nuevo_pixel)
        nueva_imagen.append(fila_nueva)

    return nueva_imagen

# Definimos una imagen de ejemplo como una matriz de píxeles representados por tuplas (R, G, B)
imagen_original = [
    [(0.2, 0.4, 0.6), (0.7, 0.1, 0.9), (0.5, 0.8, 0.2)],
    [(0.8, 0.3, 0.4), (0.2, 0.6, 0.5), (0.9, 0.7, 0.1)],
    [(0.1, 0.5, 0.3), (0.4, 0.7, 0.9), (0.6, 0.2, 0.8)]
]

# Especificamos el filtro a aplicar: conservar solo el rojo y el azul, eliminar el verde
filtro = (True, False, True)

# Aplicamos el filtro a la imagen original
imagen_filtrada = aplicar_filtro(imagen_original, filtro)

# Mostramos la imagen filtrada
print("Imagen filtrada:")
for fila in imagen_filtrada:
    print(fila)

