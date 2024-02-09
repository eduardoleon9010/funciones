# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:12:47 2024

@author: USUARIO
"""

def contar_palabras(cadena: str) -> list:
    """
    Cuenta la frecuencia de cada palabra en una cadena y devuelve una lista de tuplas
    donde cada tupla contiene la palabra y su frecuencia en la cadena.

    Args:
    cadena (str): La cadena de caracteres a analizar.

    Returns:
    list: Una lista de tuplas donde cada tupla contiene una palabra y su frecuencia.
    """
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Crear un diccionario para almacenar la frecuencia de cada palabra
    frecuencia_palabras = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    # Crear una lista de tuplas con la palabra y su frecuencia
    lista_palabras_frecuencia = [(palabra, frecuencia) for palabra, frecuencia in frecuencia_palabras.items()]
    
    return lista_palabras_frecuencia

# Ejemplo de uso
cadena_ejemplo = "esto es un ejemplo de cadena de texto para contar palabras ejemplo ejemplo"
resultado = contar_palabras(cadena_ejemplo)
print("Lista de palabras y su frecuencia:", resultado)
