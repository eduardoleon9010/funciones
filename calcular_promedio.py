# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:53:50 2024

@author: USUARIO
"""

def calcular_promedio(estudiante: dict) -> float:
    """
    Calcula el promedio de un estudiante a partir de sus notas en matemáticas, lenguaje y ciencias.

    Parámetros:
    - estudiante (dict): Un diccionario que representa a un estudiante con las siguientes llaves:
        - "nombre" (str): El nombre del estudiante.
        - "matemáticas" (float): La nota en matemáticas.
        - "lenguaje" (float): La nota en lenguaje.
        - "ciencias" (float): La nota en ciencias.

    Resultado:
    - float: El promedio de las notas del estudiante.
    """
    nota_matematicas = estudiante.get("matemáticas", 0)
    nota_lenguaje = estudiante.get("lenguaje", 0)
    nota_ciencias = estudiante.get("ciencias", 0)
    promedio = (nota_matematicas + nota_lenguaje + nota_ciencias) / 3.0
    return promedio

# Solicitar información al usuario por consola
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nota_matematicas = float(input("Ingrese la nota de Matemáticas: "))
nota_lenguaje = float(input("Ingrese la nota de Lenguaje: "))
nota_ciencias = float(input("Ingrese la nota de Ciencias: "))

# Crear diccionario con la información proporcionada por el usuario
estudiante_usuario = {
    "nombre": nombre_estudiante,
    "matemáticas": nota_matematicas,
    "lenguaje": nota_lenguaje,
    "ciencias": nota_ciencias
}

# Calcular y mostrar el promedio
promedio_usuario = calcular_promedio(estudiante_usuario)
print(f"El promedio de {estudiante_usuario['nombre']} es: {promedio_usuario}")
