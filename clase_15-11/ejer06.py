class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} hace un sonido.")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Miau.")

# Crear instancia de la clase derivada
mi_gato = Gato("Pelusa")
mi_gato.hablar()