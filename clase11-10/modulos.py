#import math
from math import pi as p

def area_circulo(r):
    # return math.pi * r**2
    return p * r**2

print(f"Circulo radio 3 = {area_circulo(3):.4f}")