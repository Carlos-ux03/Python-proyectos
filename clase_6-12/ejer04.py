"""
Escribe un programa en Python que haga lo siguiente:

Solicite al usuario que introduzca una frase.
Muestre:
La cantidad total de caracteres en la frase.
La cantidad de palabras en la frase.
La frase en mayúsculas.
La frase en minúsculas.
La frase al revés.
Si la frase es un palíndromo (se lee igual al derecho y al revés, ignorando espacios y mayúsculas/minúsculas).
"""
# Solicitar al usuario una frase
frase = input("Introduce una frase: ")

# Procesar la frase
num_caracteres = len(frase)
num_palabras = len(frase.split())
mayusculas = frase.upper()
minusculas = frase.lower()
al_reves = frase[::-1]

# Verificar si es un palíndromo (sin espacios y en minúsculas)
frase_limpia = ''.join(frase.lower().split())
es_palindromo = frase_limpia == frase_limpia[::-1]

# Mostrar resultados
print("\nResultados:")
print(f"Cantidad total de caracteres: {num_caracteres}")
print(f"Cantidad de palabras: {num_palabras}")
print(f"Frase en mayúsculas: {mayusculas}")
print(f"Frase en minúsculas: {minusculas}")
print(f"Frase al revés: {al_reves}")
print(f"¿Es un palíndromo? {'Sí' if es_palindromo else 'No'}")