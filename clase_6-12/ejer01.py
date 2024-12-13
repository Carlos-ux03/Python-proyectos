def es_anagrama(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas.
    :param palabra1: Primera palabra.
    :param palabra2: Segunda palabra.
    :return: True si son anagramas, False en caso contrario.
    """
    # Normalizamos las palabras: convertimos a minúsculas y eliminamos espacios.
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    # Comparamos las letras ordenadas de ambas palabras.
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra o frase: ")
    palabra2 = input("Ingrese la segunda palabra o frase: ")

    if es_anagrama(palabra1, palabra2):
        print(f"'{palabra1}' y '{palabra2}' son anagramas.")
    else:
        print(f"'{palabra1}' y '{palabra2}' no son anagramas.")