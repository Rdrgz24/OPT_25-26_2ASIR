"""
Crea un programa que:
1. Defina una lista vacía compras.
2. Pida al usuario 5 productos y los añada a la lista con append().
3. Muestre la lista completa.
4. Pida al usuario un producto a eliminar y lo quite con remove().
5. Muestre la lista ordenada alfabéticamente con sort().
6. Incluya un docstring explicando qué hace el programa.
"""

"""El programa pide 5 productos con una variable que incluye un input junto a split
para que el usuario pueda introducir los productos de una sola vez.
En base a estos productos, se muestran por pantalla, luego se pide eliminar uno de ellos
y se vuelve a mostrar los valores por pantallas ordenados alfabéticamente."""
# Definir la lista vacía
compras = []
# Pedir datos con input.split() permite introducir varios caracteres separados por espacio.
datos = input("Introduce 5 productos separados por espacio -> ").split()
# Única condición, ¿Has introducido 5 datos? -> Sigue
# ¿Has introducido más o menos? -> Te lo hace saber
if len(datos) == 5:
    # Añade elementos a la lista en base a la posición de los elementos recogidos en el input.
    compras.append(datos[0])
    compras.append(datos[1])
    compras.append(datos[2])
    compras.append(datos[3])
    compras.append(datos[4])
    print(compras)
    eliminar = input("Introduce el producto a eliminar -> ")
    # Elimina el elemento pasado como elemento.
    compras.remove(eliminar)
    # Ordena la lista alfabéticamente.
    compras.sort()
    print(compras)
else:
    print("Debes introducir 5 productos, no más, ni menos.")
