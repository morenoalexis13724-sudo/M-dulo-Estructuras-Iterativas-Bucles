nombre = "ELKIN ALEXIS MORENO ROJAS"
vocales = "AEIOUaeiou"
mensaje_vocales = ""

for letra in nombre:
    if letra in vocales:
        mensaje_vocales += letra.upper()

print(f"Vocales extraídas del nombre: {mensaje_vocales}")
