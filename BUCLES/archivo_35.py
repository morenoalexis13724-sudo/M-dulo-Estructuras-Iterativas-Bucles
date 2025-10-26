nombre = "ELKIN ALEXIS MORENO ROJAS"
mensaje = ""

for i in range(len(nombre)):
    if i % 3 == 0:
        mensaje += nombre[i]

print(f"Letras del nombre en posiciones múltiplo de 3: {mensaje}")
