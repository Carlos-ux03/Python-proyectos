class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @staticmethod
    def crear_cuadrado(lado):
        # Usa el mismo constructor pero para crear un cuadrado (ancho y alto iguales)
        return Rectangulo(lado, lado)

# Crear instancias
rectangulo = Rectangulo(4, 6)
cuadrado = Rectangulo.crear_cuadrado(5)

print(f"Rectángulo: Ancho = {rectangulo.ancho}, Alto = {rectangulo.alto}")
print(f"Cuadrado: Lado = {cuadrado.ancho}, Lado = {cuadrado.alto}")