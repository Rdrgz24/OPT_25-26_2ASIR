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
    print(f"Lista actual: {compras}") # Imprime nombres actuales de la lista.
    # Pide el usuario a eliminar mediante un input.
    eliminar = input("Introduce el producto a eliminar -> ")
    # Si el usuario está en la lista, lo borra, lo ordena alfabéticamente y lo muestra,
    # de lo contrario,, si no está, lo hace saber por pantalla.
    if eliminar in compras:
        compras.remove(eliminar)
        compras.sort()
        print(f"Lista tras eliminar: {compras}")
    else:
        print("Usuario no está en la lista")
else:
    print("Debes introducir 5 productos, no más, ni menos.")