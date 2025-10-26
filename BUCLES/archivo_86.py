# ELKIN ALEXIS MORENO ROJAS
numero = 1
while numero <= 10:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"{numero}! = {factorial}")
    numero += 1
