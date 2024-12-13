"""Ejercicio 04
Escriba un programa que haga la tabla de multiplicar de cualquier entero numero dado por el usuario.
La tabla debe ser de 0 al 12.
"""
nro = int(input("Escriba un nro: "))

for i in range(0, 13):
    print(f"{nro} x {i} = {nro * i}")