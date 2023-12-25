"""
Este código generará un gráfico que muestra cómo varía la velocidad final en función del 
tiempo para diferentes valores de aceleración. Puedes ajustar los valores de aceleración 
y la velocidad inicial para ver cómo afectan la velocidad final en el tiempo.

"""

import matplotlib.pyplot as plt

# Función para calcular la velocidad final
def calcular_velocidad_final(velocidad_inicial: float, aceleracion: float, tiempo: float) -> float:
    return velocidad_inicial + (aceleracion * tiempo)

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
