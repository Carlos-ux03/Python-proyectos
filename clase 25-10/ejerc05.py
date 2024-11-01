"""Ejercicio 05
Escriba un programa que genere una lista de numeros aleatorios entre 1 y 100
"""

def aleatorio():
    import random
    return random.randint(1, 10)
lista = [aleatorio() for i in range(10)]
print(lista)

s = set(lista)
print(s)
s.add(11)
s.add(2)
print(s)