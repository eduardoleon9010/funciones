def calcular_velocidad_final(velocidad_inicial: float, aceleracion: float, tiempo: float) -> float:
    """
    Calcula la velocidad final de un objeto.

    Parameters:
    velocidad_inicial (float): La velocidad inicial del objeto.
    aceleracion (float): La aceleración experimentada por el objeto.
    tiempo (float): El tiempo transcurrido.

    Returns:
    float: La velocidad final calculada del objeto.
    """
    return velocidad_inicial + (aceleracion * tiempo)
