"""

"""

opcion = int(input("Escoge una opcion [1] Registrarse [2] Iniciar sesión [3] Salir -> "))

while opcion in [1, 2, 3]:
    match opcion:
        case 1:
            print("Opcion 1")
            break
        case 2:
            print("Opcion 2")
            break
        case 3:
            print("Saliste del menú")
            break
else:
    print("Opcion no disponible")

