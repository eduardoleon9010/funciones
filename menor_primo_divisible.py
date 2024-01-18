# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:34:44 2024

@author: USUARIO
"""

def menor_primo_divisible(numero: int) -> int:
    """
    Encuentra el menor de los primeros diez números primos por el cual un número dado es divisible.

    Parámetros:
    - numero (int): Número para verificar su divisibilidad.

    Retorna:
    - int: El menor de los primeros diez números primos por el cual el número es divisible,
           o -1 si no es divisible por ninguno de esos números.
    """
    # Lista de los primeros diez números primos
    primeros_diez_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Verificar divisibilidad por los primeros diez números primos
    for primo in primeros_diez_primos:
        if numero % primo == 0:
            return primo

    # Si no es divisible por ninguno, retornar -1
    return -1

# Ejemplo de uso:
numero_dado = int(input("Ingrese un número para verificar su divisibilidad: "))

resultado = menor_primo_divisible(numero_dado)

if resultado != -1:
    print(f"El número es divisible por el menor de los primeros diez primos: {resultado}")
else:
    print("El número no es divisible por ninguno de los primeros diez primos.")
