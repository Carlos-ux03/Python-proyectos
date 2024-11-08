"""
Ejercicio 01
Escribir un programa que pida al usuario adivinar un numero entre 1 y 100
"""
import random

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en un número entre 1 y 100.")

while True:
    # Solicita la entrada del usuario
    suposicion = int(input("Adivina el número: "))
    intentos += 1

    # Compara la suposición con el número secreto
    if suposicion < numero_secreto:
        print("Demasiado bajo")
    elif suposicion > numero_secreto:
        print("Demasiado alto")
    else:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break
    