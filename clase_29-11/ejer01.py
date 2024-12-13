"""
Calcular el perimeto y area de un triangulo
"""
import math
# Función para calcular el perímetro de un triángulo
def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

# Función para calcular el área de un triángulo (fórmula de Herón)
def area_triangulo(lado1, lado2, lado3):
    s = (lado1 + lado2 + lado3) / 2
    return math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

# Función para determinar si es un triángulo
def es_triangulo(lado1,lado2,lado3):    
    return lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1

def main():
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    if es_triangulo(lado1,lado2,lado3):
        print(f"Perimetro de un Triangulo es: {perimetro_triangulo(lado1,lado2,lado3):.2f}")
        print(f"Area de un Triangulo es: {area_triangulo(lado1,lado2,lado3):.2f}")
    else:
        print("No es un triangulo")
    
if __name__ == "__main__":
    main()