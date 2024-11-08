"""Ejercicio 06
Crear una lista que el tamaño debe introducir el usuario y que luego se rellene de forma aleatoria del 1 al 100
"""
from random import randint
a = list()
tam = int(input("Introduce el tamaño de la lista: "))

for i in range(tam):
    a.append(randint(1, 100))
print(a)
print(sorted(a))