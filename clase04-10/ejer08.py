"""_summary_
Operaciones con cadenas
Introduzca una cadena y muestre en minusculas y mayusculas
divide la cadena en una lista
"""

cadena = input("Cadena: ") # ingresar cadena

mayus = cadena.upper() # poner en mayuscula
minus = cadena.lower() # poner en minuscula
cap = cadena.capitalize() # Capitalizar

print(mayus) # imprimir
print(minus) # imprimir
print(cap)  # imprimir

lista = cadena.split("o") # dividir la cadena en una lista divida por "o"

print(lista) # imprimir lista