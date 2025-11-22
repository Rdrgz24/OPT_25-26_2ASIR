"""
1. Crea una lista con al menos 5 frutas.
2. Muestra la primera y la última fruta.
3. Cambia una fruta por otra.
4. Añade una nueva fruta al final con append().
5. Elimina una fruta con remove().
6. Muestra la lista final en pantalla.
"""

frutas = ["Plátano", "Naranja", "Pera", "Manzana", "Aguacate"]

# Mostrando datos actuales de la lista
print(frutas)
# Mostrando primera y última fruta
print(frutas[0])
print(frutas[-1])
# Cambiando de posición fruta 0 (Plátano) con fruta 3 (Manzana).
frutas[0], frutas[3] = frutas[3], frutas[0]
# Añadimos una nueva fruta con append.
frutas.append("Kiwi")
# Borramos una de las frutas de la lista con remove.
frutas.remove("Pera")
# Mostramos por pantalla el valor final.
print(frutas)