# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:08:53 2024

@author: USUARIO
"""

def calcular_frecuencia_digitos(numero: int) -> dict:
    """
    Calcula un diccionario con la frecuencia de cada dígito en un número entero.

    Parámetros:
    - numero (int): El número entero del cual se calculará la frecuencia de los dígitos.

    Retorno:
    - dict: Un diccionario donde las llaves son los dígitos y los valores son la cantidad de veces que aparecen en el número.
    """
    # Inicializar el diccionario vacío para almacenar la frecuencia de cada dígito
    frecuencia_digitos = {}

    # Convertir el número a una cadena para iterar a través de sus dígitos
    for digito in str(abs(numero)):
        # Incrementar la frecuencia del dígito en el diccionario
        frecuencia_digitos[digito] = frecuencia_digitos.get(digito, 0) + 1

    return frecuencia_digitos

# Ejemplo de uso
numero_ejemplo = int(input("Escribe el numero a calucular: "))
diccionario_frecuencia = calcular_frecuencia_digitos(numero_ejemplo)

# Imprimir el resultado
print(f"Frecuencia de dígitos en el número {numero_ejemplo}: {diccionario_frecuencia}")
