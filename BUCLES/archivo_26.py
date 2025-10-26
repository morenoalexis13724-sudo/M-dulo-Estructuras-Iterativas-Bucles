nombre = "ELKIN ALEXIS MORENO ROJAS"
letras_unicas = []

for letra in nombre:
    if letra not in letras_unicas and letra != " ":
        letras_unicas.append(letra)

print(f"Número de letras únicas (sin espacios): {len(letras_unicas)}")
