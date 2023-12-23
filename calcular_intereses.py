def calcular_interes():
    try:
        capital = float(input("Ingrese la cantidad de dinero en pesos: "))
        tasa_interes = float(input("Ingrese la tasa de interés (en decimal, por ejemplo, 0.045 para 4.5%): "))
        anos = int(input("Ingrese el número de años: "))

        capital_final = capital * (1 + tasa_interes) ** anos

        print(f"Después de {anos} años, el capital inicial de {capital} pesos con una tasa de interés del {tasa_interes * 100}%")
        print(f"se convierte en {capital_final:.2f} pesos.")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

calcular_interes()
