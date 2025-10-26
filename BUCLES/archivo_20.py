nombre = "ELKIN ALEXIS MORENO ROJAS"
contador_espacios = 0

for letra in nombre:
    if letra == " ":
        contador_espacios += 1

print(f"El nombre tiene {contador_espacios} espacios.")
