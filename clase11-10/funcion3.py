
def calculo(x,y):
    pe = (x+y)*2
    print("llamando funcion...")
    return pe

a = int(5)
b = int(3)
print(f"Lado=5, ancho=3 perimetro: {calculo(a,b)}")
print(f"Lado=10.2, ancho=3.5 perimetro: {calculo(10.2,3.5)}")