nombre = "ELKIN ALEXIS MORENO ROJAS"
contador_vocales = 0
contador_consonantes = 0

for letra in nombre.upper():
    if letra in "AEIOU":
        contador_vocales += 1
    elif letra.isalpha():
        contador_consonantes += 1

print(f"Vocales: {contador_vocales}, Consonantes: {contador_consonantes}")
