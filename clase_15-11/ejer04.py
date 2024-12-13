class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def mostrar_edad(self):
        print(f"{self.nombre} tiene {self.edad} años.")

# Crear una instancia de la clase
mi_perro = Perro("Rex", 5)
mi_perro.ladrar()
mi_perro.mostrar_edad()