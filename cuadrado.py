def cuadrado(x: float) -> float:
    """
    Calcula el cuadrado de un número dado.

    Parámetros:
    x (float): El número del cual se desea calcular el cuadrado.

    Retorna:
    (float): El cuadrado del número proporcionado.
    """
    return x ** 2


# Programa principal
print(cuadrado(2))  # Calcula el cuadrado de 2 y muestra el resultado (4)
a = 1 + cuadrado(3)  # Calcula el cuadrado de 3, le suma 1 y asigna el resultado a 'a' (10)
print(cuadrado(a * 3))  # Calcula el cuadrado de 'a' multiplicado por 3 (100)


def cubo(x: float) -> float:
    """
    Calcula el cubo de un número dado.

    Parámetros:
    x (float): El número del cual se desea calcular el cubo.

    Retorna:
    (float): El cubo del número proporcionado.
    """
    return x * x * x


y = 2
print(cubo(y))  # Imprime el resultado del cubo de 2


def area_rectangulo(altura: float, ancho: float) -> float:
    """
    Calcula el área de un rectángulo dada su altura y ancho.

    Parámetros:
    altura (float): La altura del rectángulo.
    ancho (float): El ancho del rectángulo.

    Retorna:
    (float): El área del rectángulo con los valores proporcionados.
    """
    return altura * ancho


x = float(input("Digite la altura: "))
y = float(input("Digite el ancho: "))
area = area_rectangulo(x, y)
print("El área del rectángulo es:", area)


def leer_entero() -> int:
    """
    Solicita al usuario que ingrese un número entero y lo devuelve.

    Retorna:
    (int): El número entero ingresado por el usuario.
    """
    return int(input("Introduce un número entero: "))


a = leer_entero()
print("El entero que ingresaste es:", a)

