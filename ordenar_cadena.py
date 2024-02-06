# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:12:19 2024

@author: USUARIO
"""

def ordenar_cadena(cadena):
    """
    Ordena alfabéticamente una cadena de caracteres compuesta únicamente del alfabeto inglés en minúsculas.

    Parameters:
    - cadena (str): La cadena de texto por ordenar.

    Returns:
    - str: La cadena que se recibió por parámetro, ordenada alfabéticamente.
    """
    # Convertir la cadena a una lista de caracteres y ordenarla
    cadena_ordenada = ''.join(sorted(cadena))

    return cadena_ordenada

# Ejemplo de uso
cadena_ejemplo = "bca"
resultado = ordenar_cadena(cadena_ejemplo)
print(f"La cadena '{cadena_ejemplo}' ordenada alfabéticamente es: '{resultado}'")
