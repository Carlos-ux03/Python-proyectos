import math

# Función para calcular el perímetro de un polígono regular
def perimetro_poligono(lado, num_lados):
    return lado * num_lados

# Función para calcular el área de un polígono regular
def area_poligono(lado, num_lados):
    apotema = lado / (2 * math.tan(math.pi / num_lados))
    perimetro = perimetro_poligono(lado, num_lados)
    return (perimetro * apotema) / 2

# Función para pentágono
def perimetro_pentagono(lado):
    return perimetro_poligono(lado, 5)

def area_pentagono(lado):
    return area_poligono(lado, 5)

# Función para hexágono
def perimetro_hexagono(lado):
    return perimetro_poligono(lado, 6)

def area_hexagono(lado):
    return area_poligono(lado, 6)

# Función para heptágono
def perimetro_heptagono(lado):
    return perimetro_poligono(lado, 7)

def area_heptagono(lado):
    return area_poligono(lado, 7)

# Función para octágono
def perimetro_octagono(lado):
    return perimetro_poligono(lado, 8)

def area_octagono(lado):
    return area_poligono(lado, 8)

# Menú principal
def main():
    print("Cálculo de perímetros y áreas de polígonos regulares")
    print("1. Pentágono")
    print("2. Hexágono")
    print("3. Heptágono")
    print("4. Octágono")
    print("5. Salir")

    while True:
        opcion = int(input("\nSeleccione una opción: "))
        if opcion == 1:
            lado = float(input("Ingrese la longitud del lado del pentágono: "))
            print(f"Perímetro del pentágono: {perimetro_pentagono(lado):.2f}")
            print(f"Área del pentágono: {area_pentagono(lado):.2f}")
        elif opcion == 2:
            lado = float(input("Ingrese la longitud del lado del hexágono: "))
            print(f"Perímetro del hexágono: {perimetro_hexagono(lado):.2f}")
            print(f"Área del hexágono: {area_hexagono(lado):.2f}")
        elif opcion == 3:
            lado = float(input("Ingrese la longitud del lado del heptágono: "))
            print(f"Perímetro del heptágono: {perimetro_heptagono(lado):.2f}")
            print(f"Área del heptágono: {area_heptagono(lado):.2f}")
        elif opcion == 4:
            lado = float(input("Ingrese la longitud del lado del octágono: "))
            print(f"Perímetro del octágono: {perimetro_octagono(lado):.2f}")
            print(f"Área del octágono: {area_octagono(lado):.2f}")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()