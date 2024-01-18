# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:40:55 2024

@author: USUARIO
"""
def puede_participar_universidad(anio_nacimiento: int, anio_entrada_universidad: int) -> bool:
    """
    Determina si una persona puede participar en una competencia universitaria.

    Parámetros:
    - anio_nacimiento (int): Año de nacimiento de la persona.
    - anio_entrada_universidad (int): Año de entrada a la universidad.

    Retorna:
    - bool: True si la persona puede participar, False en caso contrario.
    """
    # Año actual
    anio_actual = 2024  # Puedes ajustar este valor según el año actual

    # Edad de la persona
    edad = anio_actual - anio_nacimiento

    # Tiempo en la universidad
    tiempo_universidad = anio_actual - anio_entrada_universidad

    # Verificar las condiciones para participar
    if (edad < 23 or (edad == 23 and anio_entrada_universidad <= anio_actual)) and tiempo_universidad < 2:
        return True
    else:
        return False

# Ejemplo de uso:
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
anio_entrada_universidad = int(input("Ingrese el año de entrada a la universidad: "))

puede_participar = puede_participar_universidad(anio_nacimiento, anio_entrada_universidad)

if puede_participar:
    print("La persona puede participar en la competencia universitaria.")
else:
    print("La persona no cumple con los requisitos para participar.")

