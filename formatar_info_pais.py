# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:38:14 2024

@author: USUARIO
"""

def formatar_info_pais(nombre_pais, poblacion_millones, pib_usd_millones):
    """
    Formatea la información de un país para mostrarla en tres columnas.

    Parámetros:
    - nombre_pais: Nombre del país.
    - poblacion_millones: Cantidad de habitantes en millones.
    - pib_usd_millones: Producto Interno Bruto en millones de USD.

    Retorna:
    Una cadena de caracteres que representa la información del país en el formato especificado.

    Ejemplo de uso:
    resultado = formatar_info_pais("Colombia", 45, 336599)
    print(resultado)
    """
    # Formatea la primera columna (alineada a la izquierda, 25 caracteres)
    columna1 = f"{nombre_pais:<25}"

    # Formatea la segunda columna (centrada, 25 caracteres)
    columna2 = f"= {poblacion_millones} millones = "

    # Formatea la tercera columna (alineada a la derecha, 10 caracteres + espacio "USD Million")
    columna3 = f"{pib_usd_millones:>10,} USD Million"

    # Une las columnas en una sola cadena
    resultado = f"{columna1}{columna2}{columna3}"

    return resultado

# Ejemplo de uso:
nombre_pais = "Colombia"
poblacion_millones = 45
pib_usd_millones = 336599

resultado = formatar_info_pais(nombre_pais, poblacion_millones, pib_usd_millones)
print(resultado)

