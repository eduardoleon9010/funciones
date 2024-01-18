# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:22:06 2024

@author: USUARIO
"""
def determinar_ganador(nombre_equipo_A: str, nombre_equipo_B: str, goles_local_A: int, goles_visitante_B: int, goles_visitante_A: int, goles_local_B: int) -> str:
    """
    Calcula el ganador de una serie de dos partidos entre dos equipos de fútbol, considerando los goles de visitante.

    Parámetros:
    - nombre_equipo_A (str): Nombre del primer equipo.
    - nombre_equipo_B (str): Nombre del segundo equipo.
    - goles_local_A (int): Cantidad de goles que hizo el equipo A de local.
    - goles_visitante_B (int): Cantidad de goles que hizo el equipo B de visitante.
    - goles_visitante_A (int): Cantidad de goles que hizo el equipo A de visitante.
    - goles_local_B (int): Cantidad de goles que hizo el equipo B de local.

    Retorna:
    - str: Nombre del ganador de la serie o "EMPATE" en caso de empate.
    """
    # Calcular el total de goles de cada equipo considerando los goles de visitante
    total_goles_A = goles_local_A + (goles_visitante_A * 2)
    total_goles_B = goles_local_B + (goles_visitante_B * 2)

    # Determinar el ganador o si hay empate
    if total_goles_A > total_goles_B:
        return nombre_equipo_A
    elif total_goles_A < total_goles_B:
        return nombre_equipo_B
    else:
        return "EMPATE"

# Ejemplo de uso:
nombre_equipo_A = input("Ingrese el nombre del primer equipo: ")
nombre_equipo_B = input("Ingrese el nombre del segundo equipo: ")
goles_local_A = int(input("Ingrese los goles que hizo {} de local: ".format(nombre_equipo_A)))
goles_visitante_B = int(input("Ingrese los goles que hizo {} de visitante: ".format(nombre_equipo_B)))
goles_visitante_A = int(input("Ingrese los goles que hizo {} de visitante: ".format(nombre_equipo_A)))
goles_local_B = int(input("Ingrese los goles que hizo {} de local: ".format(nombre_equipo_B)))

ganador = determinar_ganador(nombre_equipo_A, nombre_equipo_B, goles_local_A, goles_visitante_B, goles_visitante_A, goles_local_B)
print(f"El ganador de la serie es: {ganador}")

