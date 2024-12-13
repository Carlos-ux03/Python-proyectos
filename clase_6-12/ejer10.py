"""
Escriba un programa que llene una lista de forma aleatoria con 10 elementos entre 1 y 100.
Crea otra lista con los numeros pares de la primera lista
Crea otra lista con los numeros impares de la primera lista
Mostrar:
El tamaño de la primera lista
El tamaño de la segunda lista
El tamaño de la tercera lista
El contenido de la primera lista
El contenido de la segunda lista
El contenido de la tercera lista
El promedio de la primera lista
El promedio de la segunda lista
El promedio de la tercera lista
"""
import random

# Crear lista de 10 elementos aleatorios entre 1 y 100
aleatorios = [random.randrange(1, 101) for _ in range(10)]

# Crear lista de elementos pares de la primera lista
pares = [num for num in aleatorios if num % 2 == 0]

# Crear lista de elementos impares de la primera lista
impares = [num for num in aleatorios if num % 2 != 0]

# Mostrar resultados
print("Tamaño primera lista:", len(aleatorios))
print("Tamaño segunda lista:", len(pares))
print("Tamaño tercera lista:", len(impares))
print("Contenido primera lista:", aleatorios)
print("Contenido segunda lista:", pares)
print("Contenido tercera lista:", impares)
print("Promedio primera lista:", sum(aleatorios)/len(aleatorios))
print("Promedio segunda lista:", sum(pares)/len(pares) if len(pares) > 0 else 0)
print("Promedio tercera lista:", sum(impares)/len(impares) if len(impares) > 0 else 0)