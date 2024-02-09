# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:33:40 2024

@author: USUARIO
"""

def generar_imagen_negra(ancho: int) -> list:
    """
    Genera una imagen completamente negra representada como una lista de listas de tuplas RGB.

    Parámetros:
        ancho (int): El ancho de la imagen en píxeles.

    Retorna:
        list: Una lista de listas de tuplas RGB que representa la imagen negra.
    """
    imagen = []
    for i in range(0, ancho):
        fila = []
        for j in range(0, ancho):
            rojo = 0.0
            verde = 0.0
            azul = 0.0
            pixel = (rojo, verde, azul)
            fila.append(pixel)
        imagen.append(fila)
    return imagen

# Ejemplo de uso
ancho_imagen = 5
imagen_negra = generar_imagen_negra(ancho_imagen)
print(imagen_negra)
