# Este script introduce las partes básicas de Python con ejemplos prácticos.

# Declaración de variables
# En Python no necesitas especificar el tipo de la variable, se asigna automáticamente.
nombre = "Juan"  # Cadena de texto
edad = 25         # Entero
altura = 1.75     # Flotante
es_estudiante = True  # Booleano

# Imprimir en consola
print("Hola,", nombre, "- Tu edad es:", edad)

# Estructuras de control
# Condicionales
if edad > 18:
    print("Eres mayor de edad.")
elif edad == 18:
    print("Tu edad es 18.")
else:
    print("Eres menor de edad.")

# Bucles
# Bucle 'for' para recorrer una lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print("Número:", numero)

# Bucle 'for' para generar una lista
par = [ c for c in range(2, 11, 2) ]
print(par)

# Bucle 'while' con condición
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1  # Incremento

# Funciones
# Definimos una función para sumar dos números
def suma(a, b):
    """
    Función que toma dos números y devuelve su suma.
    """
    return a + b

# Llamamos a la función y mostramos el resultado
resultado = suma(10, 5)
print("Suma de 10 y 5 es:", resultado)

# Manejo de listas
# Agregar elementos a una lista
frutas = ["manzana", "banana", "naranja"]
frutas.append("pera")  # Agrega 'pera' al final
print("Lista de frutas:", frutas)

# Acceder a elementos
print("Primera fruta:", frutas[0])  # Índices empiezan en 0

# Cortar listas (slicing)
print("Primeras dos frutas:", frutas[:2])  # Desde el inicio hasta el índice 2 (sin incluirlo)

# Diccionarios (estructuras clave-valor)
persona = {
    "nombre": "Juan",
    "edad": 25,
    "altura": 1.75
}
print("Información de la persona:", persona)
print("Nombre:", persona["nombre"])  # Accediendo por clave

# Operaciones matemáticas básicas
# Suma
a = 5
b = 2
suma = a + b
print("Suma de", a, "+", b, "=", suma)

# Resta
a = 5
b = 2
resta = a - b
print("Resta de", a, "-", b, "=", resta)

# Multiplicación
a = 5
b = 2
multiplicacion = a * b
print("Multiplicación de", a, "*", b, "=", multiplicacion)

# División
a = 10
b = 2
division = a / b
print("División de", a, "/", b, "=", division)

# MOdulo
a = 10
b = 3
modulo = a % b
print("Modulo de", a, "%", b, "=", modulo)

# Potencia
a = 4
b = 3
c = 1/2
potencia = a ** b
raiz = a ** c
print("Potencia de", a, "^", b, "=", potencia)
print("Raiz de", a, "^", c, "=", raiz)


# Manejo de errores con try-except
try:
    division = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

# Importar módulos
# Python tiene una gran cantidad de módulos estándar. Aquí un ejemplo con 'math'.
import math
raiz = math.sqrt(16)  # Calcula la raíz cuadrada de 16
print("Raíz cuadrada de 16:", raiz)



# Clase y objetos (POO básica)
class Persona:
    """
    Clase que representa a una persona.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Ana", 30)
persona1.saludar()