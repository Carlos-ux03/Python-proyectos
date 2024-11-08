import random

def rand():
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

if __name__ == "__main__":
    while True:
        rand()
        op = int(input("0 - Continuar jugando.\n1 - Salir\n_"))
        if op != 0:
            break