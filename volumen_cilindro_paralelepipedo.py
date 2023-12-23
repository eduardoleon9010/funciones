""" 
volumen_cilindro(radio_base, altura): Calcula el volumen de un cilindro utilizando la fórmula matemática correspondiente: 
Volumen = Area de la base × Altura. Esta función toma el radio de la base y la altura como argumentos y retorna el volumen del cilindro.

volumen_paralelepipedo(a, b, c): Calcula el volumen de un paralelepípedo, que es un sólido con seis caras paralelas opuestas y 
rectangulares, 
multiplicando el área de la base por la altura. Esta función toma tres lados del paralelepípedo como argumentos y retorna su volumen.

Luego, el código solicita al usuario ingresar los valores necesarios para calcular el volumen de un cilindro y de un paralelepípedo 
respectivamente, y muestra los resultados obtenidos a través de las funciones previamente definidas.
"""

def volumen_cilindro(radio_base: float, altura: float)->float:
    area_base = 3.1416 * radio_base * radio_base
    return area_base * altura

def volumen_paralelepipedo(a: float, b: float, c: float)->float:
    area_base = a * b
    return area_base * c


print("Calculando el volumen del cilindro...")
r = float(input("Digite el radio: "))
a = float(input("Digite la altura: "))
print("El volumendel cilindro es: ", str(volumen_cilindro(r, a)))

print("Calculando el volumen del paralelepipedo...")
ancho = float(input("Digite el ancho: "))
profundidad = float(input("Digite la profundidad: "))
altura = float(input("Digite la altura: "))
print("El volumen del palelepipedo es: ",
      str(volumen_paralelepipedo(ancho, profundidad, altura)))
