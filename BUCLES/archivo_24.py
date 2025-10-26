nombre = "ELKIN ALEXIS MORENO ROJAS"
contador_consonantes = 0
consonantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

for letra in nombre:
    if letra in consonantes:
        contador_consonantes += 1

print(f"El nombre tiene {contador_consonantes} consonantes.")
