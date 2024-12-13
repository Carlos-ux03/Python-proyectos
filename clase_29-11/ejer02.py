import math

# Función para calcular el perímetro de un cuadrado
def perimetro_cuadrado(lado):
    return 4 * lado

# Función para calcular el área de un cuadrado
def area_cuadrado(lado):
    return lado * lado

def main():
    lado = float(input("Lado del Cuadrado: "))
    perimetro = perimetro_cuadrado(lado)
    area = area_cuadrado(lado)
    print(f"El perimetro del cuadrado es : {perimetro:.2f}")
    print(f"El area del cuadrado es: {area:.2f}")

if __name__ == "__main__":
    main()