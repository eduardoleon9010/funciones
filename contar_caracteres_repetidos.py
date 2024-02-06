# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:00:07 2024

@author: USUARIO
"""

def contar_caracteres_repetidos(cadena):
    """
    Cuenta la cantidad de caracteres diferentes que aparecen más de una vez en una cadena.

    Parameters:
    - cadena (str): La cadena por revisar. Supone que todas las letras son minúsculas del alfabeto en inglés.

    Returns:
    - int: La cantidad de caracteres diferentes que aparecen repetidos en la cadena.
    """
    # Inicializar un conjunto para almacenar caracteres únicos que aparecen más de una vez
    caracteres_repetidos = set()

    # Inicializar un conjunto para almacenar caracteres únicos que ya han sido vistos
    caracteres_vistos = set()

    # Iterar sobre la cadena
    for char in cadena:
        # Verificar si el carácter ya ha sido visto
        if char in caracteres_vistos:
            # Si ya ha sido visto, agregarlo al conjunto de caracteres repetidos
            caracteres_repetidos.add(char)
        else:
            # Si no ha sido visto, agregarlo al conjunto de caracteres vistos
            caracteres_vistos.add(char)

    # La cantidad de caracteres diferentes que aparecen repetidos es la longitud del conjunto de caracteres repetidos
    return len(caracteres_repetidos)

# Ejemplo de uso
cadena_ejemplo = "abracadabra"
resultado = contar_caracteres_repetidos(cadena_ejemplo)
print(f"En la cadena '{cadena_ejemplo}', hay {resultado} caracteres diferentes que aparecen más de una vez.")
