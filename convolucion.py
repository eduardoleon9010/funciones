# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:12:39 2024

@author: USUARIO
"""

def convolucion(imagen: list, mascara: list) -> list:
    """
    Aplica una operación de convolución sobre una imagen utilizando una máscara especificada.

    Args:
    imagen (list): Matriz que representa la imagen, donde cada elemento es una tupla de 3 flotantes entre 0 y 1
                   representando los valores R, G y B del píxel.
    mascara (list): Matriz cuadrada de números que representa la máscara de convolución.

    Returns:
    list: Matriz que representa la imagen con la operación de convolución aplicada.
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    tamano_mascara = len(mascara)
    mitad_mascara = tamano_mascara // 2  # Redondeo hacia abajo para obtener el índice central

    imagen_nueva = []

    for i in range(alto):
        fila_nueva = []
        for j in range(ancho):
            suma_colores = [0, 0, 0]
            suma_coeficientes = 0

            # Iteramos sobre los elementos de la máscara y los píxeles vecinos
            for x in range(tamano_mascara):
                for y in range(tamano_mascara):
                    # Coordenadas del píxel vecino
                    fila_vecina = i - mitad_mascara + x
                    columna_vecina = j - mitad_mascara + y

                    # Verificamos si estamos dentro de los límites de la imagen
                    if (0 <= fila_vecina < alto) and (0 <= columna_vecina < ancho):
                        coeficiente = mascara[x][y]
                        suma_coeficientes += coeficiente

                        pixel_vecino = imagen[fila_vecina][columna_vecina]
                        for k in range(3):
                            suma_colores[k] += pixel_vecino[k] * coeficiente

            # Calculamos los nuevos valores de los componentes RGB
            nuevos_colores = []
            for suma_color in suma_colores:
                if suma_coeficientes != 0:
                    nuevos_colores.append(suma_color / suma_coeficientes)
                else:
                    nuevos_colores.append(suma_color)

            # Asignamos el nuevo píxel a la imagen
            fila_nueva.append(tuple(nuevos_colores))

        imagen_nueva.append(fila_nueva)

    return imagen_nueva

# Ejemplo de uso
# Definimos una máscara de convolución
mascara = [
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]

# Definimos una imagen de ejemplo
imagen_original = [
    [(0.2, 0.4, 0.6), (0.7, 0.1, 0.9), (0.5, 0.8, 0.2)],
    [(0.8, 0.3, 0.4), (0.2, 0.6, 0.5), (0.9, 0.7, 0.1)],
    [(0.1, 0.5, 0.3), (0.4, 0.7, 0.9), (0.6, 0.2, 0.8)]
]

# Aplicamos la convolución a la imagen original
imagen_convolucionada = convolucion(imagen_original, mascara)

# Mostramos la imagen convolucionada
print("Imagen convolucionada:")
for fila in imagen_convolucionada:
    print(fila)
