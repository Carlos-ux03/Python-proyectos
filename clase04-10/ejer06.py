"""_summary_
funciones de la lista
"""
lista = [1,2,3,4,5,6,7,"Hola", "Chau", True]

print(1 in lista) # ver si existe 1 en la lista
tupla = (10,20,30,40,50,60)
print(1 in tupla) # ver si existe 1 en la tupla

list1 = [5, 6, 3, 10, 4, 9, 1, 7,11]
print(list1)
list1.sort() # organiza de menor a mayor
print(list1)
list1.sort(reverse=True) # organiza de mayor a menor
print(list1)

t1 = tuple(list1)
print(t1)

list1.append(8)
print(list1)

t1 = tuple(list1)
print(t1)