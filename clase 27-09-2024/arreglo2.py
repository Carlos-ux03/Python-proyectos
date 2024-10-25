a = []

t = int(input("Cuantos valores desea agregar al arreglo?: "))

for i in range(t):
    e = int(input("registrar valor: "))
    a.append(e)

print(a)

b = []

while True:
    e = int(input("valor: "))
    b.append(e)
    o = input("continuar (s/n): ")
    if o == "n":
        break

print(b)