"""Ejercicio 05
Crear una lista que el tamaño debe introducir el usuario y que luego se rellene por el usuario
"""

a = list()
#print(a)
tam = int(input("Introduce el tamaño de la lista: "))
if tam == 0:
    tam = 1

for i in range(tam):
    a.append(int(input("Introduce un valor: ")))
print(a)

print(sorted(a)) # funcion para ordenar

if 6 in a: # busca si existe el elemento en la lista
    print("hay nro 6")
else:
    print("No hay nro 6")