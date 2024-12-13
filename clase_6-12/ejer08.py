"""
Contador de palabras unicas
"""
def contar_palabras_unicas(oracion):
    # Convertir todo a minúsculas para evitar duplicados por mayúsculas/minúsculas
    palabras = oracion.lower().split()
    # Eliminar puntuación básica de las palabras
    palabras_limpias = [''.join(char for char in palabra if char.isalnum()) for palabra in palabras]
    # Crear un conjunto para obtener palabras únicas
    palabras_unicas = set(palabras_limpias)
    # Ordenar las palabras únicas alfabéticamente
    palabras_ordenadas = sorted(palabras_unicas)
    return palabras_ordenadas, len(palabras_ordenadas)

# Solicitar al usuario una oración
oracion = input("Introduce una oración: ")

# Contar palabras únicas
palabras_ordenadas, total_unicas = contar_palabras_unicas(oracion)

# Mostrar los resultados
print("\nResultados:")
print(f"Total de palabras únicas: {total_unicas}")
print("Palabras únicas ordenadas alfabéticamente:")
print(", ".join(palabras_ordenadas))