# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:19:21 2024

@author: USUARIO
"""

from mpmath import mp

def calcular_phi_con_precision_maxima():
    """
    Calcula phi (φ) con la mayor precisión posible.

    Retorna:
    - str: La representación en cadena de phi con máxima precisión.
    """
    mp.dps += 100000  # Incrementar la precisión para obtener más decimales
    phi = mp.phi
    return str(phi)

# Calcular phi con la máxima precisión posible
resultado_maxima_precision = calcular_phi_con_precision_maxima()
print(f"Phi con la máxima precisión posible: {resultado_maxima_precision}")
