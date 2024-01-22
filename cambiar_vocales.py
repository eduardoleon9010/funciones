# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:51:57 2024

@author: USUARIO
"""
def cambiar_vocales(cadena: str, letra: str) -> str:
    """
    Cambia todas las vocales de una cadena por una letra específica.

    Parámetros:
    - cadena (str): La cadena original.
    - letra (str): La letra con la cual se reemplazarán las vocales.

    Retorna:
    str: La cadena modificada con las vocales reemplazadas por la letra especificada.
    """
    # Crear una lista con los caracteres modificados
    resultado = [letra if char.lower() in 'aeiou' else char for char in cadena]
    # Unir la lista en una cadena nuevamente
    resultado_cadena = ''.join(resultado)
    return resultado_cadena

# Ejemplo de uso
cadena_original = "Hola, Mundo!"
letra_a_usar = 'I'
resultado_final = cambiar_vocales(cadena_original, letra_a_usar)
print(resultado_final)
