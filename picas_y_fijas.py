# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:33:33 2024

@author: USUARIO
"""

def contar_picas(num_secreto: int, num_propuesto: int) -> int:
    """
    Calcula la cantidad de picas entre un número secreto y un número propuesto en el juego Picas y Fijas.

    Parámetros:
    - num_secreto (int): Número secreto de 4 dígitos.
    - num_propuesto (int): Número propuesto de 4 dígitos.

    Retorna:
    - int: Cantidad de picas entre los dos números.
    """
    # Convertir los números a listas de dígitos
    digitos_secreto = [int(d) for d in str(num_secreto)]
    digitos_propuesto = [int(d) for d in str(num_propuesto)]

    # Inicializar el contador de picas
    picas = 0

    # Verificar la cantidad de picas comparando los dígitos
    for digito in digitos_propuesto:
        if digito in digitos_secreto:
            picas += 1

    return picas


def contar_fijas(num_secreto: int, num_propuesto: int) -> int:
    """
    Calcula la cantidad de fijas entre un número secreto y un número propuesto en el juego Picas y Fijas.

    Parámetros:
    - num_secreto (int): Número secreto de 4 dígitos.
    - num_propuesto (int): Número propuesto de 4 dígitos.

    Retorna:
    - int: Cantidad de fijas entre los dos números.
    """
    # Convertir los números a listas de dígitos
    digitos_secreto = [int(d) for d in str(num_secreto)]
    digitos_propuesto = [int(d) for d in str(num_propuesto)]

    # Inicializar el contador de fijas
    fijas = 0

    # Verificar la cantidad de fijas comparando los dígitos en la misma posición
    for i in range(len(digitos_secreto)):
        if digitos_secreto[i] == digitos_propuesto[i]:
            fijas += 1

    return fijas


# Ejemplo de uso:
num_secreto = 5678
num_propuesto = 6579

picas = contar_picas(num_secreto, num_propuesto)
fijas = contar_fijas(num_secreto, num_propuesto)

print(f"Resultado: {picas} picas y {fijas} fijas")
