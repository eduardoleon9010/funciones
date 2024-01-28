# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:16:13 2024

@author: USUARIO
"""

def mejor_camara_con_nombres(celulares: dict, nombre1: str, nombre2: str) -> str:
    """
    Busca cuál de los dos celulares tiene la mejor cámara.

    Parámetros:
    - celulares (dict): Un diccionario donde las llaves son los nombres de los celulares
      y los valores son diccionarios que representan características de los celulares.
    - nombre1 (str): El nombre del primer celular que se quiere comparar.
    - nombre2 (str): El nombre del segundo celular que se quiere comparar.

    Retorno:
    - (str): Retorna el nombre del celular que tiene la mejor cámara o "Empate" si
      las cámaras de los dos celulares son iguales.
      Si sólo uno de los nombres corresponde al de un celular, retorna ese nombre.
      Si ningún nombre corresponde al de un celular, retorna "Nombres inválidos".
    """

    # Extraer los celulares del diccionario usando su nombre
    celular1 = celulares.get(nombre1, None)
    celular2 = celulares.get(nombre2, None)

    # Ninguno de los dos nombres era correcto
    if celular1 is None and celular2 is None:
        nombre_mejor = "Nombres inválidos"

    # Sólo el segundo nombre era correcto
    elif celular1 is None and celular2 is not None:
        nombre_mejor = nombre2

    # Sólo el primer nombre era correcto
    elif celular1 is not None and celular2 is None:
        nombre_mejor = nombre1

    # Los dos nombres eran correctos, así que comparar las cámaras de los celulares
    else:
        nombre_mejor = "Empate"
        camara_celular1 = celular1.get('camara', 0)
        camara_celular2 = celular2.get('camara', 0)

        if camara_celular1 > camara_celular2:
            nombre_mejor = nombre1
        elif camara_celular1 < camara_celular2:
            nombre_mejor = nombre2

    return nombre_mejor


# Ejemplo de uso
celulares_dict = {
    'iPhone': {'camara': 12, 'pantalla': 6.1, 'bateria': 3000},
    'Samsung': {'camara': 16, 'pantalla': 6.4, 'bateria': 3500},
    'Huawei': {'camara': 12, 'pantalla': 6.0, 'bateria': 4000}
}

nombre_ganador = mejor_camara_con_nombres(celulares_dict, 'iPhone', 'Samsung')
print(f"El celular con la mejor cámara es: {nombre_ganador}")
