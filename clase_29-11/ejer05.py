import math
# Función para verificar si los lados pertenecen a un triángulo
from ejer01 import es_triangulo
# Función para calcular el perímetro de un triángulo
from ejer01 import perimetro_triangulo
# Función para calcular el área de un triángulo (fórmula de Herón)
from ejer01 import area_triangulo
# Función para calcular el perímetro de un cuadrado
from ejer02 import perimetro_cuadrado
# Función para calcular el área de un cuadrado
from ejer02 import area_cuadrado
# Función para calcular el perímetro y área de un rectángulo
import ejer03
# Función para calcular el perímetro y área de un círculo
import ejer04

# Menú principal
def main():
    print("Cálculo de perímetros y áreas de polígonos")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Círculo")
    print("5. Salir")

    while True:
        opcion = int(input("\nSeleccione una opción: "))
        if opcion == 1:
            lado1 = float(input("Ingrese el lado 1: "))
            lado2 = float(input("Ingrese el lado 2: "))
            lado3 = float(input("Ingrese el lado 3: "))
            if es_triangulo(lado1,lado2,lado3):
                print(f"Perímetro del triángulo: {perimetro_triangulo(lado1, lado2, lado3):.2f}")
                print(f"Área del triángulo: {area_triangulo(lado1, lado2, lado3):.2f}")
            else:
                print("No es un triangulo")
        elif opcion == 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            print(f"Perímetro del cuadrado: {perimetro_cuadrado(lado):.2f}")
            print(f"Área del cuadrado: {area_cuadrado(lado):.2f}")
        elif opcion == 3:
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            print(f"Perímetro del rectángulo: {ejer03.perimetro_rectangulo(largo, ancho):.2f}")
            print(f"Área del rectángulo: {ejer03.area_rectangulo(largo, ancho):.2f}")
        elif opcion == 4:
            ejer04.main()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()