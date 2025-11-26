""" El programa pide al usuario añadir tres claves junto a tres valores, con la condición de que
el teléfono debe ser de 9 dígitos. Asigna estos contactos a un diccionario llamado agenda
y permite UNA vez buscar UN usuario para mostrar su teléfono en base a su nombre."""

# Declarar el diccionario agenda vacío.
agenda = {}
# Blucle for que se recorre tres veces para lso tres usuarios.
for i in range(3):
    # Pide nombre y teléfono.
    nombre = input("Introduce el nombre -> ")
    telf = input("Introduce el teléfono (9 dígitos) -> ")
    #Si el teléfono tiene 9 dígitos se asigna dentro de agenda[clave] = valor
    # Dentro del diccionario, por ejemplo agenda[pepe] = 556677889
    # De lo contrario indica que el formato es incorrecto y pide el siguiente usuario.
    if len(telf) == 9:
        agenda[nombre] = telf
    else:
        print("Formato teléfono incorrecto, no se registrará usuario.")

# Bucle for para recorrer los items del diccionario por clave y valor (nombre : telf)
for nombre, telf in agenda.items():
    print(f"{nombre} : {telf}")

#Tras mostrar toda la lista de contactos, se busca el nombre introducido por pantalla.
busqueda = input("Introduce el nombre del usuario a buscar -> ")

# Si el usuario introducido está dentro de la agenda, lo muestra, de lo contrario lo indica.
if busqueda in agenda:
    print(f"Teléfono del usuario {busqueda} : {agenda[busqueda]}")
else:
    print("Contacto no encontrado.")