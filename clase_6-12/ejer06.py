"""
Escribe un programa en Python que analice una cadena ingresada por el usuario y determine cuántas vocales, consonantes y otros caracteres (como espacios, números o símbolos) contiene.
"""
def contar_caracteres(cadena):
    vocales = "aeiouáéíóúü"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    
    num_vocales = 0
    num_consonantes = 0
    otros = 0
    
    for caracter in cadena.lower():
        if caracter in vocales:
            num_vocales += 1
        elif caracter in consonantes:
            num_consonantes += 1
        else:
            otros += 1
    
    return num_vocales, num_consonantes, otros

# Solicitar al usuario una cadena
cadena = input("Introduce una cadena: ")

# Contar vocales, consonantes y otros caracteres
vocales, consonantes, otros = contar_caracteres(cadena)

# Mostrar los resultados
print("\nResultados:")
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")
print(f"Número de otros caracteres: {otros}")