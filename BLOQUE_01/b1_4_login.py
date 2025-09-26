#Crea un script que:
# · Guarde en variables:
# usuario_correcto = "admin"
# contrasena_correcta = "1234"
# · Pida al usuario con input() un nombre y contraseña.
# · Use operadores de comparación y lógicos para verificar:
# -> Si ambos coinciden → mostrar "Acceso concedido".
# -> Si no → mostrar "Acceso denegado".

usuario_correcto = "admin"
contrasena_correcta = "1234"

tu_usuario = input("Ingresa usuario -> ")
tu_contrasena = input("Ingresa contraseña -> ")

if usuario_correcto == tu_usuario and contrasena_correcta == tu_contrasena:
    print("Acceso condedido")
else:
    print("Acceso denegado")