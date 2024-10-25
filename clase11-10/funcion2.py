lista = ["Ana", "Eduardo", "Luis", "Juan", "Pedro", "Briam", "John"]
tupla = tuple(lista)
sets = set(lista)
def saludar(x="Mundo"):
    print(f"Hola, {x}!")

saludar()
for i in lista:
    saludar(i)

# for i in tupla:
#     saludar(i)

# for i in sets:
#     saludar(i)

print("-------------------------------------")
def sal(x):
    return f"Hola, {x}!"

s = [sal(i) for i in lista]
# print(s)

for i in s:
    print(i)