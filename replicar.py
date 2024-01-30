# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:16:31 2024

@author: USUARIO
"""
def replicar(cadena: str, cantidad: int = 2) -> str:
    """
    Replica una cadena dada un número de veces y devuelve la cadena resultante.

    Parámetros:
    - cadena (str): La cadena que se replicará.
    - cantidad (int): Número de veces que se replicará la cadena. Por defecto, es 2.

    Resultado:
    - str: Una cadena que contiene la replicación de la cadena original.
    """
    return cadena * cantidad

# Ejemplo de uso:
resultado = replicar("Hola", 3)
print(resultado)  # Imprime 'HolaHolaHola'
