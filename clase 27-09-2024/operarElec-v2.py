"""_summary_
Crear un algoritmo que pida dos números y me de la suma, la resta, la multiplicación y la división segun la opcion elegida
"""

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

print("Elija que opercion desea hacer:")
print("1 - Suma, 2 - Resta, 3 - Producto, 4 - Cociente")
op = int(input("Opcion: "))

match op:
    case 1:
        print(f"La suma de {a} + {b} = {a+b}")
    case 2:
        print(f"La resta de {a} - {b} = {a-b}")
    case 3:
        print(f"El producto de {a} * {b} = {a*b}")
    case 4:
        if b == 0: print("No se puede dividir por Cero..!!")
        else:
            print(f"El cociente de {a} / {b} = {a/b}")
    case _:
        print("La operacion no es valida")
        
# ejemplo de match
""" def consulta():
    return (1, 4180000, "Ana", "Lezcano", 234, 236)
w = consulta
match w:
    case (1,4180000,"Ana", "Lezcano",234, 236):
        print("encontrado")
    case _:
        print("valore no encontrado") """