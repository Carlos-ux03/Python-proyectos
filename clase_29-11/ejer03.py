import math

# Función para calcular el perímetro de un rectángulo
def perimetro_rectangulo(lado, ancho):
    return (lado + ancho)* 2

# Función para calcular el área de un rectángulo
def area_rectangulo(lado, ancho):
    return lado * ancho

def main():
    lado = float(input("Lado del Rectangulo: "))
    ancho = float(input("Ancho del Rectangulo: "))
    perimetro = perimetro_rectangulo(lado, ancho)
    area = area_rectangulo(lado, ancho)
    print(f"El perimetro del rectángulo es : {perimetro:.2f}")
    print(f"El area del rectángulo es: {area:.2f}")

if __name__ == "__main__":
    main()