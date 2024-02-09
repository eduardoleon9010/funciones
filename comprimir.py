# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:14:28 2024

@author: USUARIO
"""

def comprimir(cadena: str) -> tuple:
    """
    Comprime una cadena de ceros y unos encontrando las secuencias de unos y devolviendo
    una tupla con la longitud original de la cadena y una lista de tuplas con la posición
    y el tamaño de cada secuencia de unos.

    Args:
    cadena (str): La cadena de ceros y unos a comprimir.

    Returns:
    tuple: Una tupla con la longitud original de la cadena y una lista de tuplas
    con la posición y el tamaño de cada secuencia de unos.
    """
    longitud_original = len(cadena)
    secuencias = []
    i = 0
    while i < len(cadena):
        if cadena[i] == '1':
            inicio = i
            longitud = 0
            while i < len(cadena) and cadena[i] == '1':
                longitud += 1
                i += 1
            secuencias.append((inicio, longitud))
        else:
            i += 1
    return longitud_original, secuencias

# Ejemplo de uso
cadena_ejemplo = '101101111000110'
resultado = comprimir(cadena_ejemplo)
print("Resultado de la compresión:", resultado)
