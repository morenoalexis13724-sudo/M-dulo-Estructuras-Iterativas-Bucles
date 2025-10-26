nombre = "ELKIN ALEXIS MORENO ROJAS"
contador = 0

for letra in nombre:
    if letra.lower() in "aeiou":
        contador += 1
        print(f"Vocal número {contador}")
