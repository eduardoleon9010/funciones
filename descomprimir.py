# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:15:59 2024

@author: USUARIO
"""

def descomprimir(resultado: tuple) -> str:
    """
    Descomprime una tupla devuelta por la función comprimir para producir la cadena original.

    Args:
    resultado (tuple): Una tupla con la longitud original de la cadena y una lista de tuplas
    con la posición y el tamaño de cada secuencia de unos.

    Returns:
    str: La cadena original antes de ser comprimida.
    """
    longitud_original, secuencias = resultado
    cadena_descomprimida = ['0'] * longitud_original
    for inicio, longitud in secuencias:
        for i in range(inicio, inicio + longitud):
            cadena_descomprimida[i] = '1'
    return ''.join(cadena_descomprimida)

# Ejemplo de uso
resultado_comprimir = (15, [(0, 1), (2, 2), (5, 4), (12, 2)])
cadena_original = descomprimir(resultado_comprimir)
print("Cadena original después de descomprimir:", cadena_original)
