"""
1. Crea un diccionario vacío llamado agenda.
2. Pide al usuario que introduzca 3 contactos (nombre y teléfono).
 · El nombre será la clave.
 · El teléfono será el valor.
3. Muestra la agenda completa usando un bucle.
4. Permite al usuario buscar un contacto por nombre:
 · Si existe, muestra el teléfono.
 · Si no existe, muestra "Contacto no encontrado".
5. Añade un docstring explicando qué hace el programa.
"""

agenda = {}

for i in range(3):
    nombre = input("Introduce el nombre -> ")
    telf = input("Introduce el teléfono (9 dígitos) -> ")
    if len(telf) == 9:
        agenda[nombre] = telf
    else:
        print("Formato teléfono incorrecto, no se registrará usuario.")

for nombre, telf in agenda.items():
    print(f"{nombre} : {telf}")

busqueda = input("Introduce el nombre del usuario a buscar -> ")

if busqueda in agenda:
    print(f"Teéfono del usuario {busqueda} : {agenda[busqueda]}")