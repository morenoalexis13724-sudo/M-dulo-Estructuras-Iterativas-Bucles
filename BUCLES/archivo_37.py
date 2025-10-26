nombre = "ELKIN ALEXIS MORENO ROJAS"
contador_mismo = 0

for letra in nombre:
    if letra.lower() == 'o':
        contador_mismo += 1

print(f"El nombre contiene la letra 'o' {contador_mismo} veces.")
