class Contador:
    cuenta = 0  # Variable de clase

    def __init__(self):
        Contador.cuenta += 1

    @classmethod
    def mostrar_cuenta(cls):
        print(f"Se han creado {cls.cuenta} instancias.")

    @staticmethod
    def mensaje_estatico():
        print("Este es un método estático.")

# Crear varias instancias
a = Contador()
b = Contador()
c = Contador()

Contador.mostrar_cuenta()
Contador.mensaje_estatico()
print(a.cuenta, b.cuenta, c.cuenta)
d = Contador()
print(a.cuenta, b.cuenta, c.cuenta, d.cuenta)