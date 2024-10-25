"""
Calcular en area de un cuadrado con una función
"""
def area_cuadrado(l):
    p = l*4
    a = l**2
    print(f"el perimetro del cuadrado es: {p}")
    print(f"el area del cuadrado es: {a:.2f}")
# sale de la funcion
print(__name__)
if __name__ == '__main__':
    l = float(input("ingrese el valor de lado del cuadrado: "))
    area_cuadrado(l)