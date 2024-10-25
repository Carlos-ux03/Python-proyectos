"""_summary_
Pedir Tres valores y ver cual de ellos es el mayor
"""

a = int(input("Ingrese el número A: "))
b = int(input("Ingrese el número B: "))
c = int(input("Ingrese el número C: "))

if a > b and a > c:
    print(f"el número {a} es el mayor")
elif b > a and b > c:
    print(f"el número {b} es el mayor")
else:
    print(f"el número {c} es el mayor")