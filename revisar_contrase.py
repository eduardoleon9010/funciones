"""
Created on Mon Jan 15 08:20:36 2024

@author: USUARIO
"""

def revisar(contrasena_almacenada: str, contrasena_ingresada: str) -> str:
    """
    Compara la contraseña almacenada con la contraseña ingresada y devuelve un mensaje.

    Parameters:
    - contrasena_almacenada (str): La contraseña almacenada en algún lugar.
    - contrasena_ingresada (str): La contraseña que el usuario ingresa.

    Returns:
    - str: Un mensaje indicando si la contraseña es correcta o incorrecta.
    """
    contrasena_correcta = contrasena_almacenada == contrasena_ingresada

    if contrasena_correcta:
        mensaje = "Su contraseña es correcta"
    else:
        mensaje = "La contraseña es incorrecta"

    return mensaje

# Ejemplo de uso:
contrasena_almacenada = "secreto"
contrasena_ingresada = input("Ingrese su contraseña:")
mensaje = revisar(contrasena_almacenada, contrasena_ingresada)
print(mensaje)
