"""Funciones sobre cadenas"""

cad = input("Introduzca una cadena: ")
mayus = cad.upper()
minus = cad.lower()
print(mayus)
print(minus)
cap = cad.capitalize()
print(cap)

if cad.islower():
    print("Esta en minuscula")
elif cad.isupper():
    print("Esta en mayuscula")
elif cad.istitle():
    print("Esta en Capital")
else:
    print("Es otro")