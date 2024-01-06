caracteres = ['z', 'G', '0', '1', '2', '$', '\\']

for caracter in caracteres:
    """
    Itera a través de la lista de caracteres y muestra su respectivo número Unicode.

    Parámetros:
    caracter (str): El carácter actual en la lista.

    Proceso:
    Utiliza la función ord() para encontrar el número correspondiente en el sistema Unicode para cada carácter en la lista.
    Luego, imprime el carácter junto con su número Unicode.

    Retorna:
    None
    """
    numero_unicode = ord(caracter)
    print(f"El número Unicode para '{caracter}' es: {numero_unicode}")
