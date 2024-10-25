"""
Cadenas
"""

cadena_mas_lineas= """JavaScript es un lenguaje de programación que te permite implementar cosas complejas en páginas web. Cada vez que una página web hace algo más que sentarse ahí y mostrar información estática para que la veas — mostrando actualizaciones de contenido oportunas, mapas interactivos, gráficos animados 2D/3D, desplazando máquinas reproductoras de video, o más, puedes apostar que probablemente JavaScript esté involucrado .
"""
#print(cadena_mas_lineas)  # impresión de la cadena

existe = "Python" in cadena_mas_lineas # True si existe la cadena dentro de cadena_mas_lineas
print(f" existe: {existe}") # True si existe la cadena dentro de cadena_mas_lineas (existe)
c1 = "lenguaje" # la cadena es 'lenguaje'
c2 = "Lenguaje" # la cadena es 'Lenguaje' con una mayuscula
existe = c1.lower() in cadena_mas_lineas.lower()
print(f" existe: {existe}") # True si existe la cadena dentro de cadena_mas_lineas (existe)
existe = c2.lower() in cadena_mas_lineas.lower()
print(f" existe: {existe}") # True si existe la cadena dentro de cadena_mas_lineas (existe)