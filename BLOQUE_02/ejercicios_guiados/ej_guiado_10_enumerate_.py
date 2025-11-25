"""
1. Lista de frutas:
frutas = ["manzana", "banana", "cereza"]
2. Recorre la lista usando enumerate() y muestra:
0 manzana
1 banana
2 cereza
3. Repite el ejercicio pero usando índice empezando en 1.
"""

frutas = ["Manzana", "Melocotón", "Sandía"]

print("Lista de frutas enumeradas:")
for indice, f in enumerate(frutas):
    print(indice, f)
print("\nLista de frutas enumeradas empezando desde 1:")
for indice, f in enumerate(frutas, start=1):
    print(indice, f)