nombre = "ELKIN ALEXIS MORENO ROJAS"
contador = 0

for letra in nombre:
    if letra.lower() in "aeiou" and letra.isupper():
        contador += 1

print(f"Número de vocales en mayúscula: {contador}")
