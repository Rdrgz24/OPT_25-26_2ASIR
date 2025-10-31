"""
1. Crea una función registrar_usuario(nombre, edad, ciudad="Madrid").
2. La función debe mostrar en pantalla: "Usuario: [nombre], Edad: [edad], Ciudad: [ciudad]".
3. Debe poder llamarse con:
 · Todos los argumentos posicionales.
 · Algún argumento omitido, usando el valor por defecto.
 · Argumentos nombrados en distinto orden.
4. Incluye un docstring en la función.
5. Desde el programa principal, llama a la función al menos 3 veces con diferentes combinaciones de argumentos.
"""

def registrar_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Todos los argumentos posicionales.
registrar_usuario("Rafael", 20, "Huelva")
# Algún argumento omitido, usando el valor por defecto.
registrar_usuario("Lucas", 27)
# Argumentos nombrados en distinto orden.
registrar_usuario(ciudad="Sevilla", nombre="Manuel", edad=22)