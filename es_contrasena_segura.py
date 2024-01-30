# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:56:20 2024

@author: USUARIO
"""

def es_contrasena_segura(contrasena):
    """
    Verifica si una contraseña es lo suficientemente segura.

    Parámetros:
    - contrasena (str): La contraseña a verificar.

    Resultado:
    - bool: True si la contraseña es segura, False de lo contrario.
    """
    # Restricción 1: Debe tener al menos 10 caracteres.
    if len(contrasena) < 10:
        return False

    # Restricción 2: Debe cumplir con al menos 3 de las restricciones adicionales.
    cumplidas = 0

    # Restricción 3a: Al menos una letra mayúscula y una letra minúscula.
    if any(car.isupper() for car in contrasena) and any(car.islower() for car in contrasena):
        cumplidas += 1

    # Restricción 3b: Al menos un dígito.
    if any(car.isdigit() for car in contrasena):
        cumplidas += 1

    # Restricción 3c: Al menos uno de los siguientes caracteres: !"@$%&/()=?#
    if any(car in '!"@$%&/()=?#' for car in contrasena):
        cumplidas += 1

    # Restricción 4: No puede empezar ni terminar con un espacio.
    if contrasena[0] == ' ' or contrasena[-1] == ' ':
        return False

    # Cumplir con al menos 3 restricciones adicionales.
    return cumplidas >= 3

# Ejemplo de uso:
contrasena_prueba = "Segura123!"
if es_contrasena_segura(contrasena_prueba):
    print(f"La contraseña '{contrasena_prueba}' es segura.")
else:
    print(f"La contraseña '{contrasena_prueba}' no es segura.")
