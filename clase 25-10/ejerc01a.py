""" Ejercicio 01
Escribir un programa que pida dos números y me de la suma, la resta, la multiplicación, la división y modulo por eleccion por teclado
"""
var1 = float(input("Escriba un nro: "))
var2 = float(input("Escriba un nro: "))

print("Elija que opercion desea hacer:")
print("1 - Suma, 2 - Resta, 3 - Multiplicación, 4 - División, 5 - Modulo")
op = int(input("Opcion: "))

if op == 1:
    print(f"la suma es: {var1 + var2}")
elif op == 2:
    print(f"la resta es: {var1 - var2}")
elif op == 3:
    print(f"la multiplicacion es: {var1 * var2}")
elif op == 4:
    if var2 != 0:
        print(f"la division es: {var1 / var2}")
    else:
        print("No se puede dividir por Cero..!!")
elif op == 5:
    if var2 != 0:
        print(f"el modulo es: {var1 % var2}")
    else:
        print("No se puede dividir por Cero..!!")
else:
    print("La Operacion no es valida")