"""
Encontrar las palabras mas largas
"""
def palabras_mas_largas(texto):
    palabras = texto.split()
    longitud_maxima = max(len(palabra) for palabra in palabras)
    palabras_largas = [palabra for palabra in palabras if len(palabra) == longitud_maxima]
    return palabras_largas, longitud_maxima

# Solicitar una oración al usuario
oracion = input("Introduce una oración: ")

# Encontrar palabras más largas
palabras_largas, longitud = palabras_mas_largas(oracion)

# Mostrar los resultados
print("\nResultados:")
print(f"Palabras más largas: {', '.join(palabras_largas)}")
print(f"Longitud de las palabras más largas: {longitud}")