"""
Introduzca los datos de un rectángulo y calcula su perimetro y area
perimetro = lado mas ancho por 2
area = lado por ancho
"""

lado = int(input("Introduce el valor del lado: "))
ancho = int(input("Introduce el valor del ancho: "))

perimetro = (lado + ancho) * 2 # calcula el perimetro
area = lado * ancho # calcula el area

print(f"El perimetro es: {perimetro} unidades")
print(f"El area es: {area} unidades")