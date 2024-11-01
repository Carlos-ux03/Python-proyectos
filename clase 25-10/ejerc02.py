"""Ejercicio 02
Escribir un programa que pida una cadena de caracteres y imprima la longitud de la cadena
Tambien imprimir la cadena alreves.
"""

#cad es una variable de tipo string
#input es la funcion que pide una cadena
cad = input("Introduce una cadena: ")
# funcion len() da el tamanio de la cadena
longitud = len(cad)
print("tiene",longitud, "Caracteres")
print(f"tiene {longitud} Caracteres")
# imprime la cadena alreves
print(cad[::-1])