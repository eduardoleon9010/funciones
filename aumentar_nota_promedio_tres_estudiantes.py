# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:57:57 2024

@author: USUARIO
"""

def aumentar_nota_promedio_tres_estudiantes(estudiante1: dict, estudiante2: dict, estudiante3: dict, materia: str) -> None:
    """
    Aumenta la nota de cada estudiante en una materia en un 10% del promedio de los tres estudiantes en esa materia.

    Parámetros:
    - estudiante1 (dict): Un diccionario que representa al primer estudiante.
    - estudiante2 (dict): Un diccionario que representa al segundo estudiante.
    - estudiante3 (dict): Un diccionario que representa al tercer estudiante.
    - materia (str): El nombre de la materia en la que se aumentará la nota.

    Resultado:
    - None: La función modifica los diccionarios de los estudiantes directamente.
    """
    # Verifica que la materia especificada exista en los diccionarios de los estudiantes
    if materia in estudiante1 and materia in estudiante2 and materia in estudiante3:
        # Calcula el promedio de las notas en la materia
        promedio_notas = (estudiante1[materia] + estudiante2[materia] + estudiante3[materia]) / 3.0
        # Calcula el aumento en un 10% del promedio
        aumento = 0.10 * promedio_notas

        # Aumenta la nota de cada estudiante en la materia
        estudiante1[materia] += aumento
        estudiante2[materia] += aumento
        estudiante3[materia] += aumento

        print(f"Nota en {materia} aumentada en un 10% del promedio para cada estudiante.")
    else:
        print(f"{materia} no es una materia válida para todos los estudiantes.")

# Ejemplo de uso:
estudiante1 = {"nombre": "Juan", "matemáticas": 85, "lenguaje": 90, "ciencias": 78}
estudiante2 = {"nombre": "Ana", "matemáticas": 92, "lenguaje": 88, "ciencias": 95}
estudiante3 = {"nombre": "Pedro", "matemáticas": 78, "lenguaje": 85, "ciencias": 88}

print("Estudiantes antes del aumento de notas:")
print(estudiante1)
print(estudiante2)
print(estudiante3)

materia_aumentar_notas = input("Ingrese el nombre de la materia a aumentar las notas: ")

# Llamada a la función para aumentar las notas en la materia especificada
aumentar_nota_promedio_tres_estudiantes(estudiante1, estudiante2, estudiante3, materia_aumentar_notas)

print("\nEstudiantes después del aumento de notas:")
print(estudiante1)
print(estudiante2)
print(estudiante3)

