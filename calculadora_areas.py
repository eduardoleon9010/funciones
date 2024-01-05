# Calculadora de áreas

Este repositorio contiene funciones para calcular áreas de figuras geométricas simples y obtener la diferencia entre estas áreas.

## Funciones:

### `calcular_area_cuadrado(lado: float) -> float`
Esta función calcula el área de un cuadrado dado el valor de un lado.


### `calcular_area_circulo(radio: float) -> float`
Calcula el área de un círculo dado el valor del radio.

### `calcular_diferencia(lado: float) -> float`
Esta función obtiene la diferencia entre el área de un cuadrado y un círculo, donde el cuadrado tiene el lado proporcionado y el círculo tiene la mitad de ese lado como radio.

## Uso:
```python
# Ejemplo de uso
lado_cuadrado = float(input("Digite el lado del cuadrado: "))
diferencia = calcular_diferencia(lado_cuadrado)
print("La diferencia entre el área del cuadrado y el círculo es:", round(diferencia, 2))
