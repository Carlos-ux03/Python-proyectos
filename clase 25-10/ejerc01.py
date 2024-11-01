""" Ejercicio 01
Escribir un programa que pida dos números y me de la suma, la resta, la multiplicación, la división y modulo
"""
var1 = float(input("Escriba un nro: "))
var2 = float(input("Escriba un nro: "))

suma = var1 + var2
print(f"la suma es : {suma}")
resta = var1 - var2
print(f"la resta es : {resta}")
multiplicacion = var1 * var2
print(f"la multiplicacion es : {multiplicacion}")
division = var1 / var2 if var2 != 0 else 0
print(f"la division es : {division:.2f}")
modulo = var1 % var2 if var2 != 0 else 0
print(f"el modulo es : {modulo}")