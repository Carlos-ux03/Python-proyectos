import random

# Generar un número aleatorio entre 1 y 10
n_aleatorio = random.randint(1, 10)
print(f"numero aleatorio entero: {n_aleatorio}")

# Generar un número aleatorio entre 1 y 10 con decimales
n_aleatorio = random.uniform(1, 10)
print(f"numero aleatorio decimal: {n_aleatorio}")
print(f"numero aleatorio decimal redondeado: {n_aleatorio:.2f}")

# Generar una lista de 10 números aleatorios entre 1 y 100 usando la librería random
nums = random.sample(range(1, 101), 10)
print("lista 1:",nums)

# Generar una lista de 10 números aleatorios entre 1 y 100 usando la librería random y list comprehension
num = [random.randint(1, 100) for i in range(10)]
print("lista 2:",num)

# Generar una lista de 10 números aleatorios entre 1 y 100 sin repetir usando la librería random y while
nums_sin_repetir = []
while len(nums_sin_repetir) < 10:
    num = random.randint(1, 100)
    if num not in nums_sin_repetir:
        nums_sin_repetir.append(num)
print("lista 3:",nums_sin_repetir)

# Generar una lista de 10 números aleatorios entre 1 y 100 sin repetir 
n_s = set()
while len(n_s) < 10:
    n_s.add(random.randint(1, 100))
print("lista 4:",list(n_s))

# ver si un numero no aparece en una lista
if 9 not in nums_sin_repetir:
    print("El numero 9 no aparece en la lista")
else:
    print("El numero 9 aparece en la lista")

# ver si un numero aparece en un set
if 8 in n_s:
    print("El numero 8 aparece en la lista")
else:
    print("El numero 8 no aparece en la lista")

# ver si una palabra contiene la letra i
palabra = input("Introduce una palabra: ")
if "i" in palabra:
    print(f"La letra i aparece {palabra.count("i")} veces en la palabra {palabra}")
else:
    print(f"La letra i no aparece en la palabra {palabra}")

# ver si un nombre esta en una lista
nombres = ["pepe", "juan", "maria", "luis", "ana"]
if "pepe" in nombres:
    print("El nombre pepe esta en la lista")
else:
    print("El nombre pepe no esta en la lista")

# Generar una palabra aleatoria de 3 a 15 letras
import string
letras = string.ascii_lowercase
palabra = ''.join(random.choice(letras) for i in range(random.randint(3, 15)))
print(palabra)

nombres =["pepe", "juan", "maria", "luis", "ana"]
# Unir una lista de nombres con guiones
cad = '-'.join(nombres)
print(cad)

# Unir una lista de nombres con espacios
cad = ' '.join(nombres)
print(cad)

# Unir una lista de nombres con comas
cad = ','.join(nombres)
print(cad)

# ordenar una lista
orden = nombres.sort()
print(orden)

# invertir una lista
orden = nombres.reverse()
print(orden)

# copiar una lista
lista = nombres.copy()
print(lista)    

# concatenar dos listas 
lista1 = ["pepe", "juan", "maria", "luis", "ana"]
lista2 = ["luis", "maria", "pepe", "ana"]
lista3 = lista1 + lista2
print(lista3)   

# contar el numero de veces que aparece un elemento en una lista
print(f"hay {lista3.count("pepe")} pepes en la lista")


# eliminar un elemento de una lista
lista = ["pepe", "juan", "maria", "luis", "ana"]
lista.remove("pepe")
print(lista)