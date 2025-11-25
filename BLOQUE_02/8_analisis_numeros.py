""" En base a una lista con un for que genera un total de 20 números, el programa muestra:
el cuadrado de cada uno de ellos, pares de la lista, mayores que diez y por
último muestra el doble de cada número."""

# Declarando la lista
lista = [n for n in range(1,21)]
# Usando compresiones de listas para calcular el cuadrado.
cuadrado = [ n ** 2 for n in lista ]
# Usando compresiones de listas para calcular los pares.
par = [n for n in lista if n % 2 == 0]
# Usando compresiones de listas para calcular los mayores que diez.
masdiez = [n for n in lista if n > 10]
# Usando compresiones de listas para calcular los dobles.
doble = {n: n * 2 for n in lista }

print(f"Cuadrado de los números: {cuadrado} \nMayores que diez: {par}\nNúmeros pares de la lista: {masdiez}\nDoble de los números {doble}")