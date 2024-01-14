import matplotlib.pyplot as plt
import seaborn as sns

def visualizar_pairplot(datos):
    """
    Genera y muestra un gráfico de pares para visualizar relaciones entre variables en un conjunto de datos.

    Parámetros:
    - datos (DataFrame): El conjunto de datos a visualizar.

    Retorna:
    - None: Muestra el gráfico de pares.
    """
    sns.pairplot(datos)
    plt.show()

# Ejemplo de uso con un conjunto de datos llamado 'dataset'
visualizar_pairplot(dataset)
