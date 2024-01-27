# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:58:04 2024

@author: USUARIO
"""
def imprimir_definicion(diccionario: dict, palabra: str) -> None:
    """ Imprime la definición de una palabra o, si la palabra no existe,
    un mensaje indicando el problema.
    Parámetros:
    diccionario (dict): Un diccionario con las palabras y sus definiciones
    palabra (str): La palabra para la que se quiere la definición
    """
    definicion = diccionario.get(palabra, None)
    if definicion is not None:
        print("La definición de", palabra, "es:", definicion)
    else:
        print("La palabra '" + palabra + "' no se encuentra en el diccionario")

# Ejemplo de uso
diccionario_ejemplo = {'python': 'Un lenguaje de programación', 'diccionario': 'Una estructura de datos'}
imprimir_definicion(diccionario_ejemplo, 'python')
imprimir_definicion(diccionario_ejemplo, 'java')