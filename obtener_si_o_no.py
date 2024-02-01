# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:32:17 2024

@author: USUARIO
"""

def obtener_si_o_no(mensaje):
    """
    Solicita al usuario ingresar 'S' para sí o 'N' para no y valida la entrada.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario.

    Returns:
        str: 'S' si el usuario elige sí, 'N' si elige no.
    """
    entrada_valida = False
    respuesta = input(mensaje)
    
    while not entrada_valida:
        respuesta = respuesta.upper()  # Convertir a mayúsculas
        if respuesta == 'S' or respuesta == 'N':
            entrada_valida = True
        else:
            respuesta = input('Por favor, ingrese S para sí o N para no. \n' + mensaje)

    return respuesta

# Ejemplo de uso
respuesta_usuario = obtener_si_o_no('¿Te gusta el mani? Sí o No: ')

if respuesta_usuario == 'S':
    print('¡Excelente! Es muy saludable.')
else:
    print('Qué lástima. Si se cocina bien, es bastante sabroso.')
