""" 
Imprimir los árboles de la lista hasta que aparezca nogal.
Utiliza la variable arboles = ["manzano", "pino", "madroño", "eucalipto","nogal", "olivo", "almendro"]
"""
arboles = ["manzano", "pino", "madroño", "eucalipto","nogal", "olivo", "almendro"]
for i in arboles:
    print(i, end=" ")
    if i == "nogal":
        break