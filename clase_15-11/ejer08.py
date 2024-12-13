class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            print("Nombre no válido.")

# Uso de la propiedad
p = Persona("Carlos")
print(p.nombre)  # Accede como si fuera un atributo
p.nombre = "Ana"  # Cambia el valor usando el setter
print(p.nombre)