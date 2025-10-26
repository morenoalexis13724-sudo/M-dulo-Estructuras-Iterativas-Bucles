nombre = "ELKIN ALEXIS MORENO ROJAS"
mensaje = ""

for i, letra in enumerate(nombre):
    if i % 2 == 0:
        mensaje += letra.upper()
    else:
        mensaje += letra.lower()

print(f"Nombre con alternancia mayúsculas/minúsculas: {mensaje}")
