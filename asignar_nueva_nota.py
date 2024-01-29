# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:56:19 2024

@author: USUARIO
"""

def asignar_nueva_nota(estudiante: dict, materia: str, nueva_nota: float) -> None:
    """
    Asigna una nueva nota a un estudiante en una materia específica.

    Parámetros:
    - estudiante (dict): Un diccionario que representa a un estudiante con las siguientes llaves:
        - "nombre" (str): El nombre del estudiante.
        - "matemáticas" (float): La nota en matemáticas.
        - "lenguaje" (float): La nota en lenguaje.
        - "ciencias" (float): La nota en ciencias.
    - materia (str): El nombre de la materia a la que se le asignará la nueva nota.
    - nueva_nota (float): La nueva nota que se asignará al estudiante en la materia especificada.

    Resultado:
    - None: La función modifica el diccionario del estudiante directamente.
    """
    # Verifica que la materia especificada exista en el diccionario del estudiante
    if materia in estudiante:
        # Asigna la nueva nota a la materia correspondiente
        estudiante[materia] = nueva_nota
        print(f"Nota de {estudiante['nombre']} actualizada en {materia} a: {nueva_nota}")
    else:
        print(f"{materia} no es una materia válida para {estudiante['nombre']}.")

# Ejemplo de uso:
estudiante_ejemplo = {"nombre": "Ana", "matemáticas": 92, "lenguaje": 88, "ciencias": 95}
print("Estudiante antes de la actualización:", estudiante_ejemplo)

# Solicitar información al usuario por consola
materia_a_actualizar = input("Ingrese la materia a actualizar: ")
nueva_nota_usuario = float(input("Ingrese la nueva nota: "))

# Actualizar la nota del estudiante y mostrar el resultado
asignar_nueva_nota(estudiante_ejemplo, materia_a_actualizar, nueva_nota_usuario)
print("Estudiante después de la actualización:", estudiante_ejemplo)
