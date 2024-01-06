caracteres = ['😢', '🇨🇴', '木']  # Verifica que cada elemento sea un único carácter

for caracter in caracteres:
    """
    Itera a través de la lista de caracteres e intenta mostrar el número Unicode para cada carácter individual.

    Proceso:
    El código recorre cada elemento en la lista 'caracteres'. Luego, para cada carácter presente en ese elemento, 
    intenta obtener su número Unicode utilizando la función ord(). Posteriormente, imprime el número Unicode de 
    cada carácter individual presente en los elementos de la lista.

    Retorna:
    None
    """
    for char in caracter:
        numero_unicode = ord(char)
        print(f"El número Unicode para '{char}' es: {numero_unicode}")
