"""
1. Lista de nombres:
nombres = ["Ana", "Luis", "Marta", "Carlos"]
2. Recorre la lista usando enumerate() y muestra el índice y el nombre.
3. Convierte el resultado en lista de tuplas y muéstralo.
Salida esperada:

0 Ana
1 Luis
2 Marta
3 Carlos
[(0, 'Ana'), (1, 'Luis'), (2, 'Marta'), (3, 'Carlos')]
"""

nombres = ["Antonio", "Luis", "José María", "María José"]

for indice, n in enumerate(nombres):
    print(indice, n)

tupla = list(enumerate(nombres))
print(tupla)