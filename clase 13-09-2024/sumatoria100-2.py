"""
Desarrolle un algoritmo que realice la sumatoria de los números enteros pares comprendidos entre el 1
y el 100, es decir, 2 + 4 + 6 +…. + 100. El programa deberá imprimir los números en cuestión y
finalmente su sumatoria
"""

suma = 0
for i in range(0,101,2):
    suma+=i
# print([i for i in range(0,101,2)])
print(suma)