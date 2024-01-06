
def fahrenheit_a_centigrados(grados_f: float) -> float:
    """
    Convierte grados Fahrenheit a grados Centígrados.

    Parámetros:
    grados_f (float): Los grados Fahrenheit que se desean convertir.

    Retorna:
    (float): El valor equivalente en grados Centígrados.
    """
    grados_cent = (grados_f - 32) * (5 / 9)
    return grados_cent


def centigrados_a_fahrenheit(grados_c: float) -> float:
    """
    Convierte grados Centígrados a grados Fahrenheit.

    Parámetros:
    grados_c (float): Los grados Centígrados que se desean convertir.

    Retorna:
    (float): El valor equivalente en grados Fahrenheit.
    """
    grados_f = (grados_c * 9 / 5) + 32
    return grados_f


def radianes_grados(radianes: float) -> float:
    """
    Convierte radianes en grados.

    Parámetros:
    radianes (float): Los radianes que se desean convertir a grados.

    Retorna:
    (float): El valor equivalente en grados.
    """
    pi = 3.14159
    return (360 * radianes) / (2 * pi)


def grados_a_radianes(grados: float) -> float:
    """
    Convierte grados en radianes.

    Parámetros:
    grados (float): Los grados que se desean convertir a radianes.

    Retorna:
    (float): El valor equivalente en radianes.
    """
    pi = 3.14159
    rad = (2 * pi * grados) / 360
    return rad


def invertir_numero(numero: int) -> int:
    """
    Recibe un número entero positivo de cifras (4) y devuelve el número invertido.

    Parámetros:
    numero (int): El número que se desea invertir.

    Retorna:
    (int): El número invertido.
    """
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    millares = numero % 10
    
    inverso = str(unidades) + str(decenas) + str(centenas) + str(millares)
    return int(inverso)

