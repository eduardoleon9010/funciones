import matplotlib.pyplot as plt

def calcular_velocidad_final(velocidad_inicial: float, aceleracion: float, tiempo: float) -> float:
    """
    Calcula la velocidad final en función de la velocidad inicial, la aceleración y el tiempo.

    Parámetros:
    - velocidad_inicial (float): La velocidad inicial.
    - aceleracion (float): La aceleración aplicada.
    - tiempo (float): El tiempo transcurrido.

    Returns:
    float: La velocidad final calculada.
    """
    resultado = velocidad_inicial + (aceleracion * tiempo)
    print(f"La velocidad final para la aceleración {aceleracion} en el tiempo {tiempo} es: {resultado}")
    return resultado

# Valores iniciales para la velocidad y el tiempo
velocidad_inicial = 32.2  # Ejemplo de una velocidad inicial específica
tiempos = list(range(0, 100))  # Lista de tiempos

# Diferentes aceleraciones para graficar
aceleraciones = [2.0, 4.0, 6.0]  # Valores arbitrarios de aceleración

plt.figure(figsize=(10, 6))

# Graficar la velocidad final para cada aceleración
for aceleracion in aceleraciones:
    velocidades_finales = [calcular_velocidad_final(velocidad_inicial, aceleracion, tiempo) for tiempo in tiempos]
    plt.plot(tiempos, velocidades_finales, label=f'Aceleración: {aceleracion}')

plt.xlabel('Tiempo')
plt.ylabel('Velocidad final')
plt.title('Variación de la velocidad final en función del tiempo y la aceleración')
plt.legend()
plt.grid(True)
plt.show()





