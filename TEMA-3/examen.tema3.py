# Continuando con el código anterior...

# Lista aleatoria ya generada
lista_aleatoria = llenar_lista_aleatoria(13, 1, 99)

# Crear una lista para almacenar los números múltiplos de 3
lista_multiplos_de_3 = []

# Iterar sobre cada elemento de la lista aleatoria
for numero in lista_aleatoria:
    # Si el número es múltiplo de 3, agregarlo a la lista
    if numero % 3 == 0:
        lista_multiplos_de_3.append(numero)

# Imprimir la lista de números múltiplos de 3
print("Lista de números múltiplos de 3:", lista_multiplos_de_3)

# Continuando con el código anterior...

# Lista aleatoria ya generada
lista_aleatoria = llenar_lista_aleatoria(13, 1, 99)

# Crear una lista para almacenar los números pares
lista_pares = []

# Iterar sobre cada elemento de la lista aleatoria
for numero in lista_aleatoria:
    # Si el número es par, agregarlo a la lista de pares
    if numero % 2 == 0:
        lista_pares.append(numero)

# Imprimir la lista de números pares
print("Lista de números pares:", lista_pares)

# Continuando con el código anterior...

# Lista aleatoria ya generada
lista_aleatoria = llenar_lista_aleatoria(13, 1, 99)

# Crear una lista para almacenar los números impares
lista_impares = []

# Iterar sobre cada elemento de la lista aleatoria
for numero in lista_aleatoria:
    # Si el número es impar, agregarlo a la lista de impares
    if numero % 2 != 0:
        lista_impares.append(numero)

# Imprimir la lista de números impares
print("Lista de números impares:", lista_impares)

import random

def llenar_lista_aleatoria(tamaño, limite_inferior, limite_superior):
    """Llena una lista con números aleatorios dentro de un rango."""
    lista = []
    for _ in range(tamaño):
        numero_aleatorio = random.randint(limite_inferior, limite_superior)
        lista.append(numero_aleatorio)
    return lista

# Crear una lista aleatoria de 13 elementos entre 1 y 99
lista_aleatoria = llenar_lista_aleatoria(13, 1, 99)

# Crear una lista para almacenar los múltiplos de 3
lista_multiplos_de_3 = [num for num in lista_aleatoria if num % 3 == 0]

# Mostrar el tamaño de las listas
print("Tamaño de la lista aleatoria:", len(lista_aleatoria))
print("Tamaño de la lista de múltiplos de 3:", len(lista_multiplos_de_3))

# Mostrar el contenido de las listas
print("Lista aleatoria:", lista_aleatoria)
print("Lista de múltiplos de 3:", lista_multiplos_de_3)

# Mostrar el contenido de las listas ordenadas
print("Lista aleatoria ordenada:", sorted(lista_aleatoria))
print("Lista de múltiplos de 3 ordenada:", sorted(lista_multiplos_de_3))

# Calcular y mostrar el promedio de las listas
def calcular_promedio(lista):
    if not lista:
        return 0  # Si la lista está vacía, retorna 0
    return sum(lista) / len(lista)

print("Promedio de la lista aleatoria:", calcular_promedio(lista_aleatoria))
print("Promedio de la lista de múltiplos de 3:", calcular_promedio(lista_multiplos_de_3))