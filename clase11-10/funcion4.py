"""
Funciones con argumentos variables
"""
def varios(*var):
    for i in var:
        print(f"{i}")

varios(1)
varios(1,"dos")
varios(3,4,5)
varios("Uno", "dos", "tres", "cuatro")

def fun_c_v(**cv):
    for c,v in cv.items():
        print(f"clave: {c}, valor: {v}")
        
fun_c_v(clave1="valor1", clave2="valor2")
fun_c_v(nombre="Ana", apellido="Balbuena", edad=23)

def login(**cred):
    for c,v in cred.items():
        if c == "celular":
            print(f"Login por celular: {v}")
        elif c == "email":
            print(f"Login por email: {v}")

login(celular="595966332255",passw="0123456789", fecha="11-10-2024")
login(email="micorreo@email.co",passw="0123456789", fecha="11-10-2024")