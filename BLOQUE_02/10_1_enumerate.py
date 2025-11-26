""" En base a una lista de nombres, recorrer la lista con enumerate(), en este caso usé un bucle for,
y además mostrar el resultado en una lista de tuplas."""

# Asignamos los valores a la lista
nombres = ["Antonio", "Luis", "José María", "María José"]

# Recorremos la lista con enumerate con indice y nombre
for indice, n in enumerate(nombres):
    print(indice, n)

# Definimos una tubla para que haya "listas entre tuplas"
tupla = list(enumerate(nombres))
print(tupla)