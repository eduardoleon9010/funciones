def volumen_cilindro(radio_base: float, altura: float) -> float:
    """
    Calcula el volumen de un cilindro utilizando la fórmula Volumen = Área de la base × Altura.
    
    Parámetros:
    radio_base (float): Radio de la base del cilindro.
    altura (float): Altura del cilindro.

    Retorna:
    float: Volumen del cilindro.

    Esta función toma el radio de la base y la altura como argumentos y retorna el volumen del cilindro.
    """
    area_base = 3.1416 * radio_base * radio_base
    return area_base * altura

def volumen_paralelepipedo(a: float, b: float, c: float) -> float:
    """
    Calcula el volumen de un paralelepípedo multiplicando el área de la base por la altura.

    Parámetros:
    a (float): Lado a del paralelepípedo.
    b (float): Lado b del paralelepípedo.
    c (float): Lado c del paralelepípedo.

    Retorna:
    float: Volumen del paralelepípedo.

    Esta función toma tres lados del paralelepípedo como argumentos y retorna su volumen.
    """
    area_base = a * b
    return area_base * c

# Solicitar al usuario los valores para calcular el volumen del cilindro
print("Calculando el volumen del cilindro...")
r = float(input("Digite el radio: "))
a = float(input("Digite la altura: "))
print("El volumen del cilindro es:", str(volumen_cilindro(r, a)))

# Solicitar al usuario los valores para calcular el volumen del paralelepípedo
print("Calculando el volumen del paralelepípedo...")
ancho = float(input("Digite el ancho: "))
profundidad = float(input("Digite la profundidad: "))
altura = float(input("Digite la altura: "))
print("El volumen del paralelepípedo es:", str(volumen_paralelepipedo(ancho, profundidad, altura)))
