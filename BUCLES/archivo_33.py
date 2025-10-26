nombre = "ELKIN ALEXIS MORENO ROJAS"
resultado = 1

for letra in nombre:
    if letra != " ":
        resultado *= len(letra) + 1  

print(f"Resultado de multiplicar por cada letra: {resultado}")
