nombre = "ELKIN ALEXIS MORENO ROJAS"
contador = 0

for letra in nombre:
    if letra != " ":
        contador += 1

print(f"El nombre tiene {contador} letras (sin contar los espacios).")
