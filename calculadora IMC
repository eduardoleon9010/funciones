"""Esta función, calcular_IMC, calcula el Índice de Masa Corporal (IMC) utilizando la fórmula estándar para
 determinar la relación entre el peso y la altura de una persona.
El IMC se calcula dividiendo el peso (en kilogramos) entre el cuadrado de la altura (en metros). La altura 
proporcionada se convierte de centímetros a metros dividiendo por 100.
A continuación, se redondea el resultado a dos decimales para obtener un valor más claro y legible. El IMC es 
una medida comúnmente utilizada para evaluar si una persona tiene un peso saludable en relación con su altura.
El ejemplo de uso proporciona un peso de 70 kg y una altura de 170 cm, luego llama a la función calcular_IMC 
con estos valores y muestra el IMC calculado en la consola. """

  def calcular_IMC(peso_kg, altura_cm):
    # Convertir altura de centímetros a metros
    altura_m = altura_cm / 100
    
    # Calcular el BMI
    bmi = peso_kg / (altura_m ** 2)
    
    # Redondear el resultado a dos decimales
    bmi = round(bmi, 2)
    
    return bmi

# Ejemplo de uso:
peso = 70  # Peso en kilogramos
altura = 170  # Altura en centímetros

resultado = calcular_IMC(peso, altura)
print("Tu IMC es:", resultado)
