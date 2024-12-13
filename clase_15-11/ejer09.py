class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_cadena(cls, cadena):
        nombre, edad = cadena.split(',')
        return cls(nombre, int(edad))

# Crear instancia utilizando el método de clase
persona1 = Persona("Ana", 25)
persona2 = Persona.desde_cadena("Carlos,30")

print(f"Nombre: {persona1.nombre}, Edad: {persona1.edad}")
print(f"Nombre: {persona2.nombre}, Edad: {persona2.edad}")