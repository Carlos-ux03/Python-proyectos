"""Ejercicio 06
Escribir un programa que valide si un numero es primo o no
"""
import time

# Definición del decorador para medir el tiempo
def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos.")
        return resultado
    return envoltura

# Decoramos la función es_primo con el decorador medir_tiempo
@medir_tiempo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Entrada del número a verificar
numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")