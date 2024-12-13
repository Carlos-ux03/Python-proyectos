frases_palindromas = [
    "anita lava la tina",
    "a luna ese anula",
    "la ruta natural",
    "a mamá Roma le aviva el amor a mamá",
    "anula la luna",
    "amor a Roma",
    "oso",
    "radar",
    "reconocer",
    "aibofobia",  # miedo a los palíndromos
    "se verla al revés",
    "sometemos",
    "¿Acaso hubo búhos acá?",
    "¿Será lodo o dólares?",
    "No subas, abusón",
    "Dábale arroz a la zorra el abad",
    "Eva usaba rimel y le miraba suave",
    "yo hago yoga hoy",
    "a la catalana banal atacala",
    "¿A ti no, bonita?"]

def es_palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo.
    :param cadena: Cadena a verificar.
    :return: True si es un palíndromo, False en caso contrario.
    """
    # Normalizamos la cadena: convertimos a minúsculas y eliminamos caracteres no alfabéticos.
    cadena_limpia = ''.join(c for c in cadena.lower() if c.isalnum())
    # Comparamos la cadena con su reversa.
    return cadena_limpia == cadena_limpia[::-1]

# Ejemplo de uso
if __name__ == "__main__":
    cadena = input("Ingrese una palabra o frase: ")

    if es_palindromo(cadena):
        print(f"'{cadena}' es un palíndromo.")
    else:
        print(f"'{cadena}' no es un palíndromo.")