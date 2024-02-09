# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:44:21 2024

@author: USUARIO
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def cargar_imagen() -> np.ndarray:
    """Carga una imagen desde el teclado.
    
    Permite al usuario ingresar la ruta de la imagen desde el teclado y la carga
    utilizando la función imread de Matplotlib.
    
    Returns:
        np.ndarray: Matriz que representa la imagen en formato RGB.
    """
    while True:
        try:
            ruta_imagen = input("Ingrese la ruta de la imagen: ")
            imagen = mpimg.imread(ruta_imagen)
            if isinstance(imagen, np.ndarray) and len(imagen.shape) == 3 and imagen.shape[2] == 3:
                return imagen
            else:
                print("La imagen no tiene el formato esperado. Por favor, asegúrate de que sea una imagen RGB válida.")
        except FileNotFoundError:
            print("No se encontró el archivo. Por favor, verifica la ruta de la imagen.")
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

def visualizar_imagen(imagen: np.ndarray) -> None:
    """Muestra la imagen utilizando Matplotlib.
    
    Parameters:
        imagen (np.ndarray): Matriz que representa la imagen en formato RGB.
    """
    plt.imshow(imagen)
    plt.axis('off')  # Deshabilita los ejes
    plt.show()

def calcular_negativo(imagen: np.ndarray) -> np.ndarray:
    """Calcula el negativo de una imagen.
    
    Parameters:
        imagen (np.ndarray): Matriz que representa la imagen en formato RGB.
    
    Returns:
        np.ndarray: Matriz que representa el negativo de la imagen en formato RGB.
    """
    negativo = 255 - imagen
    return negativo

# Función para mostrar el menú
def mostrar_menu():
    print("\n---- Menú ----")
    print("1. Visualizar imagen")
    print("2. Calcular negativo de la imagen")
    print("3. Salir")

# Ejemplo de uso
imagen = cargar_imagen()
if imagen is not None:
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            visualizar_imagen(imagen)
        elif opcion == "2":
            negativo = calcular_negativo(imagen)
            visualizar_imagen(negativo)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida del menú.")
