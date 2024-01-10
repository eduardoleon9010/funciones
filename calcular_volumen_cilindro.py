# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:20:09 2024

@author: USUARIO
"""

import math

def calcular_volumen_cilindro(radio_base: float, altura: float) -> float:
    """Calcula el volumen de un cilindro a partir del radio de la base y la altura.

    Parámetros:
    radio_base (float): Radio de la base del cilindro.
    altura (float): Altura del cilindro.

    Retorna:
    float: Volumen del cilindro, redondeado a un decimal.
    """
    area_base = math.pi * radio_base**2
    volumen = area_base * altura

    return round(volumen, 1)

# Ejemplo de uso
radio = float(input("Ingrese el radio de la base del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

volumen_cilindro = calcular_volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen_cilindro}")
