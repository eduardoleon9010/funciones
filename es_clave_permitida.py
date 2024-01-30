# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:51:11 2024

@author: USUARIO
"""
def es_clave_permitida(clave):
    """
    Verifica si una clave cumple con las restricciones establecidas.

    Parámetros:
    - clave (int): Número entero de 4 dígitos.

    Resultado:
    - bool: True si la clave cumple con las restricciones, False de lo contrario.
    """
    clave_str = str(clave)

    # Restricción: El mismo dígito no puede aparecer más de dos veces.
    if any(clave_str.count(digito) > 2 for digito in clave_str):
        return False

    # Restricción: No puede haber dígitos consecutivos.
    if any(int(clave_str[i]) == int(clave_str[i + 1]) for i in range(len(clave_str) - 1)):
        return False

    # Restricción: No puede haber números que empiecen por 19, 200 ni 201.
    if clave_str.startswith(('19', '200', '201')):
        return False

    # Restricción: El número debe tener al menos tres dígitos diferentes.
    if len(set(clave_str)) < 3:
        return False

    # Si pasa todas las restricciones, la clave es permitida.
    return True

# Ejemplo de uso:
clave_ejemplo = 123467891011112113
if es_clave_permitida(clave_ejemplo):
    print(f"La clave {clave_ejemplo} es permitida.")
else:
    print(f"La clave {clave_ejemplo} no es permitida.")
