"""
1. Genera una lista con los números del 1 al 10 elevados al cuadrado usando comprensión de listas.
2. Genera otra lista con los números pares entre 1 y 20 usando comprensión de listas.
3. Crea un diccionario que relacione cada número del 1 al 5 con su cubo usando comprensión de diccionarios.
"""

# 1. Generar lista números 1 al 10

lista = [n ** 2 for n in range(1, 11)]
print(lista)  # [1, 4, 9, 16, 25]

# 2. Generar otra con números pares entre 1 y 20 usando compresion.

pares = [n for n in range(1, 21) if n % 2 == 0]
print(pares)

# 3. Crea un diccionario que relacione cada numero del 1 al 5

cubo = {n: n ** 3 for n in range(1, 6)}
print(cubo)