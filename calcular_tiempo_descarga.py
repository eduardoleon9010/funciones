# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:21:18 2024

@author: USUARIO
"""
def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int) -> int:
    """ Tiempo de descarga
    Parámetros:
    velocidad (int): Velocidad de descarga de la red, en Mbps
    tamanio_archivo (int): Tamaño del archivo a descargar, en GB
    Retorno:
    int: Tiempo estimado en minutos que toma la descarga del archivo
    """
    gb_megas = tamanio_archivo * 1000  # Convertir a megabytes
    velocidad_mbps = velocidad / 8  # Convertir a megabytes por segundo

    # Calcular tiempo en segundos y convertir a minutos
    tiempo_segundos = gb_megas / velocidad_mbps
    tiempo_minutos = tiempo_segundos / 60

    tiempo_descarga = round(tiempo_minutos)
    return f"La descarga tomará aproximadamente {tiempo_descarga} minutos."

