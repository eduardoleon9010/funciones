# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:42:50 2024

@author: USUARIO
"""

import random
import statistics

def generar_y_analizar_numeros_aleatorios(media_planeada, desviacion_estandar_planeada, cantidad_generados=15):
    """
    Genera y analiza una lista de números aleatorios distribuidos normalmente.

    Parameters:
    - media_planeada (float): Valor planeado para la media de la distribución normal.
    - desviacion_estandar_planeada (float): Valor planeado para la desviación estándar de la distribución normal.
    - cantidad_generados (int): Cantidad de números aleatorios a generar y analizar. Por defecto, es 15.

    Returns:
    - dict: Un diccionario con la información generada y analizada, incluyendo:
        - 'numeros_aleatorios': Lista de números aleatorios generados.
        - 'media_calculada': Media calculada de los números generados.
        - 'desviacion_calculada': Desviación estándar calculada de los números generados.
        - 'diferencia_media': Diferencia absoluta entre la media calculada y la planeada.
        - 'diferencia_desviacion': Diferencia absoluta entre la desviación estándar calculada y la planeada.
    """
    # Generar números aleatorios
    numeros_aleatorios = [random.normalvariate(media_planeada, desviacion_estandar_planeada) for _ in range(cantidad_generados)]

    # Calcular estadísticas
    media_calculada = statistics.mean(numeros_aleatorios)
    desviacion_calculada = statistics.stdev(numeros_aleatorios)

    # Comparar con los valores planeados
    diferencia_media = abs(media_calculada - media_planeada)
    diferencia_desviacion = abs(desviacion_calculada - desviacion_estandar_planeada)

    # Crear diccionario de resultados
    resultados = {
        'numeros_aleatorios': numeros_aleatorios,
        'media_calculada': media_calculada,
        'desviacion_calculada': desviacion_calculada,
        'diferencia_media': diferencia_media,
        'diferencia_desviacion': diferencia_desviacion
    }

    return resultados

# Ejemplo de uso:
resultados = generar_y_analizar_numeros_aleatorios(3.8, 1, 15)
print("Resultados:", resultados)
