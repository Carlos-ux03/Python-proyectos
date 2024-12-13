"""Ejercicio 01
Escribir un programa que tome tres notas de un alumno y de la nota final y su calificación.
Tenga en cuenta que la primera y segunda nota tienen peso de 30% y la tercera de 40%.
"""
def nota(nota1, nota2, nota3):
    return (nota1*0.3) + (nota2*0.3) + (nota3*0.4)

def aprobado(nota):
    if nota >= 10:
        return "Aprobado"
    else:
        return "Reprobado"

def leer_notas():
    nota1 = int(input("Introduce la primera nota: "))
    nota2 = int(input("Introduce la segunda nota: "))
    nota3 = int(input("Introduce la tercera nota: "))
    return nota1, nota2, nota3

if __name__ == "__main__":
    nota1, nota2, nota3 = leer_notas()
    notafinal = nota(nota1, nota2, nota3)
    print(f"La nota final es: {notafinal:.2f}")
    print(aprobado(notafinal))