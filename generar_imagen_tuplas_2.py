# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:37:51 2024

@author: USUARIO
"""

import random
import matplotlib.pyplot as plt

def generar_imagen_tuplas(ancho: int) -> list:
    """
    Genera una imagen representada como una lista de listas de tuplas RGB con valores aleatorios.

    Parámetros:
        ancho (int): El ancho de la imagen en píxeles.

    Retorna:
        list: Una lista de listas de tuplas RGB que representa la imagen con valores aleatorios.
    """
    factor = 1 / ancho
    imagen = []
    for i in range(0, ancho):
        fila = []
        for j in range(0, ancho):
            rojo = random.randint(0, i) / ancho
            verde = random.randint(0, j) / ancho
            azul = max(0, 1 - rojo - verde)
            pixel = (rojo * 255, verde * 255, azul * 255)
            fila.append(pixel)
        imagen.append(fila)
    return imagen

def mostrar_imagen(imagen: list):
    """
    Muestra la imagen generada.

    Parámetros:
        imagen (list): La imagen a mostrar.
    """
    plt.imshow(imagen)
    plt.axis('off')  # Oculta los ejes
    plt.show()

# Ejemplo de uso
ancho_imagen = 100
imagen_tuplas = generar_imagen_tuplas(ancho_imagen)
mostrar_imagen(imagen_tuplas)
