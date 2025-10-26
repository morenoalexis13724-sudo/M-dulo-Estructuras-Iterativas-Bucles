nombre = "ELKIN ALEXIS MORENO ROJAS"
vocales = "AEIOUaeiou"
contador_vocales = 0

for letra in nombre:
    if letra in vocales:
        contador_vocales += 1

print(f"El nombre tiene {contador_vocales} vocales.")
