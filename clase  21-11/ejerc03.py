"""
Existen dos variables, una con un nombre y otra con un apellido. Primero se ha de comprobar el nombre, si es igual a Daniel, se comprueba el apellido, si es igual a Ramos, se imprime por pantalla el texto Nombre y apellido correctos. En caso de que el nombre sea Daniel,
pero el apellido no sea Ramos, se imprime por pantalla el texto Apellido incorrecto. En caso que el nombre no sea Daniel, se imprime por pantalla el texto Usuario desconocido.
"""
nombre = "Daniel"
apellido = "Ramos"
if nombre=="Daniel" and apellido=="Ramos":
    print("Nombre y apellido correctos")
elif nombre=="Daniel" and apellido!="Ramos":
    print("Apellido incorecto")
elif nombre!="Daniel" and apellido=="Ramos":
    print("Nombre incorrecto")
else:
    print("Usuario desconocido")