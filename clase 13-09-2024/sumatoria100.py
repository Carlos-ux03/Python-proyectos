"""_summary_
Desarrolle un algoritmo que realice la sumatoria de los números enteros múltiplos de 5, comprendidos
entre el 1 y el 100, es decir, 5 + 10 + 15 +…. + 100. El programa deberá imprimir los números en
cuestión y finalmente su sumatoria
"""
suma = 0
for i in range(0, 101, 5):
    suma+=i
print(suma)