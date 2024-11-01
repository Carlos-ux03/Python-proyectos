"""Ejercicio 3 a
Escriba un programa que reciba una cantidad de numeros y devuelva el mayor
"""
def obtener_numeros():
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'q' para salir): ")
        if entrada.lower() == 'q':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return numeros
lista = obtener_numeros()
print(lista)
print("Mayor:", max(lista))
print("Menor:", min(lista))