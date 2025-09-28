# Crea un script que:
# 1. Recorra los números del 1 al 20 usando un bucle for.
# 2. Muestre cada número en la consola.
# 3. Si encuentra el número 13, debe mostrar el mensaje "Número encontrado" y detener el bucle con break.
# 👉 Pista: usa una condición if dentro del bucle y coloca break cuando se cumpla.

for i in range(1, 21):
    print(i)
    if i == 13:
        print("Número encontrado")
        break