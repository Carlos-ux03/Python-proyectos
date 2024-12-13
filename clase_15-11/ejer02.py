try:
    # Intentamos abrir y leer un archivo
    #file = open('archivo.txt', 'r')
    with open('archivo.txt', 'r') as file:
        contenido = file.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    # Se ejecuta si el archivo no se encuentra
    print("Error: El archivo no fue encontrado.")

except PermissionError:
    # Se ejecuta si no se tienen permisos para leer el archivo
    print("Error: No tiene permisos para leer el archivo.")

except Exception as e:
    # Se ejecuta para cualquier otro error no específico
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # Este bloque se ejecuta siempre, haya o no una excepción
    print("Finalizando la operación de lectura.")