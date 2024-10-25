# inicia arreglo con valores
a = [1, 2, 3, 4 , 5, 6]

# imprimir en pantalla
for i in a:
    print(i)

print(f"el tamaño del arregloes {len(a)}")
a.append(7)
print(f"el tamaño del arregloes {len(a)}")
a.append(8)
a.append(9)
a.append(10)
a.append(11)
print(f"el tamaño del arregloes {len(a)}")

print(f"valor en 0 es: {a[0]}")
print(f"valor en 5 es: {a[5]}")
print(f"valor en 10 es: {a[10]}")
# print(f"valor en 11 es: {a[11]}") # esto da error

# otro ejemplo de arreglos
b = []
print(b)
b.append("Ana")
print(b)
b.append(2)
print(b)
b.append(True)
b.append((1,"Hola", 2.5))
print(b)

# ejemplo de tuplas
c = (1,3, 5, 7)
print(c)
d = (1, 'M', "Aldo", 5332244)
print(d)