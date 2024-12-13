def analizar_cadena(cadena):
    """
    Analiza una cadena y devuelve un diccionario con los resultados.

    Args:
        cadena (str): La cadena a analizar.

    Returns:
        dict: Un diccionario con los siguientes datos:
            - vocales: Cantidad de vocales.
            - consonantes: Cantidad de consonantes.
            - otros: Cantidad de otros caracteres.
            - palabras: Cantidad de palabras.
            - tiene_que: True si contiene la palabra "que", False si no.
            - mayusculas: Cantidad de mayúsculas.
            - minusculas: Cantidad de minúsculas.
            - a: Cantidad de la letra "a".
            - f: Cantidad de la letra "f".
    """

    vocales = "aeiouáéíóú"
    consonantes = "bcdfghjklmnñpqrstvwxyz"

    resultados = {
        'vocales': 0,
        'consonantes': 0,
        'otros': 0,
        'palabras': len(cadena.split()),
        'tiene_que': 'que' in cadena.lower(),
        'mayusculas': 0,
        'minusculas': 0,
        'a': cadena.lower().count('a'),
        'f': cadena.lower().count('f')
    }

    for caracter in cadena:
        if caracter.lower() in vocales:
            resultados['vocales'] += 1
        elif caracter.lower() in consonantes:
            resultados['consonantes'] += 1
        else:
            resultados['otros'] += 1
        if caracter.isupper():
            resultados['mayusculas'] += 1
        elif caracter.islower():
            resultados['minusculas'] += 1

    return resultados

# Ejemplo de uso:
cadena = input("Ingrese una cadena: ")
resultados = analizar_cadena(cadena)

print("Resultados del análisis:")
for clave, valor in resultados.items():
    print(f"- {clave}: {valor}")