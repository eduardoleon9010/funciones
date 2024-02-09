# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:41:23 2024

@author: USUARIO
"""

def binarizar(imagen: list, umbral: int) -> None:
    """
    Binariza una imagen en escala de grises utilizando un umbral dado.

    Parámetros:
        imagen (list): La imagen representada como una lista de listas de tuplas RGB.
        umbral (int): El valor umbral para la binarización.

    Retorna:
        None
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen[i][j]
            gris = (rojo + verde + azul) // 3
            if gris < umbral:
                imagen[i][j] = (0, 0, 0)  # Negro
            else:
                imagen[i][j] = (255, 255, 255)  # Blanco

# Ejemplo de uso
imagen_gris = [
    [(100, 100, 100), (200, 200, 200), (50, 50, 50)],
    [(150, 150, 150), (75, 75, 75), (225, 225, 225)]
]
umbral = 150

print("Imagen en escala de grises original:")
print(imagen_gris)

binarizar(imagen_gris, umbral)
print("\nImagen binarizada:")
print(imagen_gris)
