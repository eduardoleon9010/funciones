# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:10:55 2024

@author: USUARIO
"""

def digito_mas_frecuente(numero: int) -> int:
    """
    Encuentra y retorna el dígito que aparece más veces en un número entero.

    Parámetros:
    - numero (int): El número entero del cual se buscará el dígito más frecuente.

    Retorno:
    - int: El dígito que aparece más veces en el número. Si hay empate, retorna cualquiera de los dígitos empatados.
    """
    # Convertir el número a una cadena para iterar a través de sus dígitos
    digitos = str(abs(numero))

    # Inicializar un diccionario para almacenar la frecuencia de cada dígito
    frecuencia_digitos = {}

    # Calcular la frecuencia de cada dígito
    for digito in digitos:
        frecuencia_digitos[digito] = frecuencia_digitos.get(digito, 0) + 1

    # Encontrar el dígito más frecuente
    digito_mas_frecuente = max(frecuencia_digitos, key=frecuencia_digitos.get)

    return int(digito_mas_frecuente)

# Ejemplo de uso
numero_ejemplo = 122345522
digito_resultante = digito_mas_frecuente(numero_ejemplo)

# Imprimir el resultado
print(f"El dígito más frecuente en el número {numero_ejemplo} es: {digito_resultante}")
