# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:58:33 2024

@author: USUARIO
"""

def jugar_picas_y_fijas(numero_secreto, intento):
    """
    Juega el juego de las Picas y Fijas y devuelve el resultado.

    Parámetros:
    - numero_secreto (str): Número de 4 cifras con dígitos diferentes a adivinar.
    - intento (str): Número de 4 cifras propuesto por el jugador.

    Resultado:
    - dict: Diccionario con las llaves "PICAS" y "FIJAS" que representan el resultado del juego.
    """
    resultado = {"PICAS": 0, "FIJAS": 0}

    # Verificar picas y fijas
    for i in range(4):
        if intento[i] == numero_secreto[i]:
            resultado["FIJAS"] += 1
        elif intento[i] in numero_secreto:
            resultado["PICAS"] += 1

    return resultado

# Ejemplo de uso:
numero_secreto = "1234"
intento_jugador = "1325"
resultado_juego = jugar_picas_y_fijas(numero_secreto, intento_jugador)

print("Resultado del juego:")
print(f"Picas: {resultado_juego['PICAS']}")
print(f"Fijas: {resultado_juego['FIJAS']}")
