"""

"""

while True:
    opcion = int(input("Escoge una opción [1] Registrarse [2] Iniciar sesión [3] Salir -> "))
    match opcion:
        case 1:
            while True:
                identifier = input("Introduce dirección de email -> ")
                contador = 0
                punto = False
                for n in identifier:
                    if n == ".":
                        punto = True
                        break
                    contador +=1
                if "@" in identifier and punto:
                    if contador >= 3:
                        if (identifier.endswith(".com")
                            or identifier.endswith(".es")
                            or identifier.endswith(".net")):
                            if any(char in "!@#$%&*?" for char in identifier.split("@")[0]):
                                print("El correo tiene carácteres no permitidos antes del @.")
                            else:
                                print("Correo registrado.")
                                while True:
                                    contraseña = input("Ahora introduce la contraseña -> ")
                        else:
                            print("Debe contener extensión .com, .es o .net")
                    else:
                        print("Debe haber 3 caracter antes del '.' intenta de nuevo.")
                else:
                    print("Correo incorrecto, vuelve a introducir...")
        case 2:
            print("Opción 2: Iniciar sesión")
            break
        case 3:
            print("Saliste del menú")
            break
        case _:
            print("Opción no disponible, elige nuevamente.")