"""
Crea un programa que cree dos listas aleatorias con 10 elementos cada una.
La primera lista solo tiene numeros pares
La segundalista solo tiene numeros impares
Y crea una tercera lista con la suma delos elementos de la primera y la segunda
"""
import random

# Crear lista de 10 elementos pares
pares = [random.randrange(0, 101, 2) for _ in range(10)]

# Crear lista de 10 elementos impares
impares = [random.randrange(1, 100, 2) for _ in range(10)]

# Crear lista de suma de pares e impares
suma = [pares[i] + impares[i] for i in range(10)]

# Mostrar lista
print("Lista de pares:  ", pares)
print("Lista de impares:", impares)
print("Lista de suma:   ", suma)