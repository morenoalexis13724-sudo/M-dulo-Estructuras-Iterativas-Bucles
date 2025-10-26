nombre = "ELKIN ALEXIS MORENO ROJAS"
mensaje = ""

for i in range(len(nombre)):
    if nombre[i] != " ":
        mensaje += nombre[i] + "-"

print(f"Nombre con guiones entre letras: {mensaje}")
