""" El programa pide al usuario añadir tres claves junto a tres valores, con la condición de que
el teléfono debe ser de 9 dígitos. Asigna estos contactos a un diccionario llamado agenda
y permite UNA vez buscar UN usuario para mostrar su teléfono en base a su nombre."""

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
    print(f"Teléfono del usuario {busqueda} : {agenda[busqueda]}")
else:
    print("Contacto no encontrado.")

# FALTA COMENTAR QUE HACE CADA BUCLE, INPUT, DICCIONARIO...