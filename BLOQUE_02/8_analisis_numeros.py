"""
Crea un programa que:

1. Genere una lista de 20 números enteros (pueden ser introducidos manualmente o generados con range).
2. Obtenga mediante comprensiones de listas:
· Una lista con los cuadrados de todos los números.
· Una lista con solo los números pares.
· Una lista con los números mayores que 10.
3. Cree un diccionario que relacione cada número con su doble.
4. Muestre en pantalla todos los resultados.
5. Incluya un docstring explicando qué hace el programa.
"""

lista = []
for n in range(1,21): lista.append(n)

cuadrado = [n ** 2 for n in lista ]
print(cuadrado)

par = [n for n in lista if n % 2 == 0]
print(par)

masdiez = [n for n in lista if n > 10]
print(masdiez)
# NO TERMINADO