# ELKIN ALEXIS MORENO ROJAS
numero = 1
while numero <= 5:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")
    numero += 1
