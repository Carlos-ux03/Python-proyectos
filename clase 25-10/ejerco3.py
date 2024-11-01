"""Ejercicio 3
Escriba un programa que reciba dos numeros y devuelva el mayor
"""
nro1 = int(input("Escriba un nro: "))
nro = int(input("Escriba un nro: "))

print(max(nro1,nro))

if nro1 > nro:
    print(nro1)
else:
    print(nro)