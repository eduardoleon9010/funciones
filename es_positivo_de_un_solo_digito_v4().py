# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:45:09 2024

@author: USUARIO
"""

def es_positivo_de_un_solo_digito_v4(x: int) -> bool:
    """
    Verifica si un número entero es positivo y tiene un solo dígito.

    Parameters:
    - x (int): Número entero a verificar.

    Returns:
    - bool: True si el número es positivo y tiene un solo dígito, False en caso contrario.
    """
    return 0 < x < 10
