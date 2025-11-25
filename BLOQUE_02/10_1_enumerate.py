""" En base a una lista de nombres, recorrer la lista con enumerate(), en este caso usé un bucle for,
y además mostrar el resultado en una lista de tuplas."""

nombres = ["Antonio", "Luis", "José María", "María José"]

for indice, n in enumerate(nombres):
    print(indice, n)

tupla = list(enumerate(nombres))
print(tupla)