"""_summary_
Crear un algoritmo que pida dos números y me de la suma, la resta, la multiplicación y la división segun la opcion elegida
"""

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

print("Elija que opercion desea hacer:")
print("1 - Suma, 2 - Resta, 3 - Producto, 4 - Cociente")
op = int(input("Opcion: "))
res = 0
if op == 1:
    res = a + b
    print(f"La suma de {a} + {b} = {res}")
elif op == 2:
    res = a-b
    print(f"La resta de {a} - {b} = {res}")
elif op== 3:
    res = a*b
    print(f"El producto de {a} * {b} = {res}")
elif op== 4:
    if b == 0:
        print("No se puede dividir por Cero..!!")
    else:
        res = a/b
        print(f"El cociente de {a} / {b} = {res}")
else:
    print(f"La Operacion {op} no es valida")