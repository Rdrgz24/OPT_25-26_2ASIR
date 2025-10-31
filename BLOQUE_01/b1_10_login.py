"""
Este programa permite registrar un usuario con un email y contraseña,
y luego iniciar sesión con él.
"""

# Definimos variables globales para poder trabajar con ellas desde todos los case.
identifier = ""
contrasena = ""

# Bucle principal del menú (1, 2, 3)
while True:
    opcion = int(input("Escoge una opción [1] Registrarse [2] Iniciar sesión [3] Salir -> "))
    match opcion:
        # Opción 1 - Registro
        case 1:
            while True: # Bucle para validar identificador (email)
                identifier = str(input("Introduce dirección de email -> "))
                # Busca la posición del ultimo punto en el correo insertado.
                punto_ext = identifier.rfind(".")
                # Validar estructura básica correo (contiene @, punto y contiene punto).
                if "@" in identifier and punto_ext:
                    # Extraer parte del correo que va antes del último punto.
                    antes_punto = identifier[:punto_ext]
                    # Valida los carácteres o longitud antes del "." (extensión).
                    if len(antes_punto) >= 3:
                        # Verificar que tiene extensión .com o .es o .net.
                        if (identifier.endswith(".com")
                                or identifier.endswith(".es")
                                or identifier.endswith(".net")):
                            # Verificar que antes del @ no haya símbolos no permitidos
                            if any(char in "!@#$%&*?" for char in identifier.split("@")[0]):
                                print("El correo tiene carácteres no permitidos antes del @.")
                            else:
                                while True: # Bucle de contraseña
                                    contrasena = str(input("Introduce la contraseña -> "))
                                    if len(contrasena) >= 8: # Contraseña con 8 o más caracteres...
                                        if contrasena.lower() != contrasena: # Comparativa para saber si tiene mayúscula...
                                            if any(num in "0123456789" for num in contrasena): # Comprobar que tiene algún número.
                                                if any(char in "!@#$%&*?" for char in contrasena): # Comprobar que tenga un símbolo especial.
                                                    print(f"Usuario", identifier, "con contraseña", contrasena, "registrados.")
                                                    # Se corta el bucle al registrar usuario y contraseña válidos.
                                                    break
                                                else:
                                                    print("Debe tener un carácter especial !@#$%&*?")
                                            else:
                                                print("Debe tener un número")
                                        else:
                                            print("La contraseña debe tener una mayúscula.")
                                    else:
                                        print("Contraseña debe tener al menos 8 dígitos.")
                                break
                        else:
                            print("Debe contener extensión .com, .es o .net")
                    else:
                        print("Debe haber 3 caracter antes del '.' intenta de nuevo.")
                else:
                    print("Correo incorrecto, vuelve a introducir...")
        case 2:
            # Comprobar que el usuario haya sido registrado anteriormente.
            if not identifier:
                print("No se ha registrado el usuario.")
            else:
                while True:
                    usuario_login = input("Introduce usuario -> ")
                    # Compara el usuario introducido con los usuarios (clave) del diccionario registrados.
                    if usuario_login != "volver":
                        if usuario_login == identifier:
                            intento = 0
                            while intento < 3:
                                contrasena_login = input(f"Introduce la contraseña de {usuario_login} -> ")
                                # Compara la contraseña introducida con el valor del usuario_login (clave).
                                # El valor internamente se representa como: "rafael": "Rafa1234@"
                                # Donde "rafael" es el usuario (clave) y "Rafa1234@" es la contraseña asociada (valor).
                                if contrasena_login == contrasena:
                                    print("Inicio de sesión exitoso.")
                                    intento = 3
                                else:
                                    intento += 1
                                    print(f"Contraseña incorrecta, intento {intento}/3.")
                                if intento == 3 and contrasena_login != contrasena:
                                    print("Demasiados intentos fallidos. Volviendo al menú.")
                            break
                        else:
                            print("Usuario no existe, si lo necesitas, escribe (volver) para ir al menú principal.")
                    else:
                        print("Volviendo al menú...")
                        break
        case 3:
            print("Saliste del menú")
            break
        case _:
            print("Opción no disponible, elige nuevamente.")