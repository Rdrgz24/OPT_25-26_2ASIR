"""Este programa permite practicar con los argumentos posicionales definiendo
una función con valores vacíos y predeterminados."""

def registrar_usuario(nombre, edad, ciudad="Madrid"):
    """Define función que registra un usuario en base a nombre, edad y ciudad (con valor por defecto)."""
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Todos los argumentos posicionales.
registrar_usuario("Rafael", 20, "Huelva")
# Algún argumento omitido, usando el valor por defecto.
registrar_usuario("Lucas", 27)
# Argumentos nombrados en distinto orden.
registrar_usuario(ciudad="Sevilla", nombre="Manuel", edad=22)