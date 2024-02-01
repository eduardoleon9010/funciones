# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:16:15 2024

@author: USUARIO
"""

from mpmath import mp

def calcular_decimales_phi(decimales):
    """
    Calcula los decimales de la constante phi (φ) con la precisión especificada.

    Parámetros:
    - decimales (int): La cantidad de decimales a calcular.

    Retorna:
    - str: La representación en cadena de los decimales de phi.
    """
    mp.dps = decimales + 2  # Añadir dos decimales adicionales para asegurar precisión
    phi = mp.phi
    return str(phi)

# Ejemplo: Calcular 10 decimales de phi
decimales = 10
resultado = calcular_decimales_phi(decimales)
print(f"Los primeros {decimales} decimales de phi son: {resultado}")
