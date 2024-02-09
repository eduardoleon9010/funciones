# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:39:52 2024

@author: USUARIO
"""

def convertir_a_grises(imagen: list) -> None:
    """
    Convierte una imagen en formato RGB a escala de grises.

    Parámetros:
        imagen (list): La imagen representada como una lista de listas de tuplas RGB.

    Retorna:
        None
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen[i][j]
            gris = (rojo + verde + azul) // 3
            imagen[i][j] = (gris, gris, gris)

# Ejemplo de uso
imagen_rgb = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
    [(128, 128, 128), (255, 255, 255), (0, 0, 0)]
]

print("Imagen RGB original:")
print(imagen_rgb)

convertir_a_grises(imagen_rgb)
print("\nImagen en escala de grises:")
print(imagen_rgb)
