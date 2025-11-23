"""
1. Crea una tupla llamada persona con los siguientes datos: nombre, edad, ciudad.
2. Desempaqueta la tupla en tres variables (nombre, edad, ciudad).
3. Muestra en pantalla un mensaje con la información.
4. Añade un docstring al inicio del programa explicando qué hace.
"""

"""El programa crea una tupla con tres elementos y la desempaqueta en tres variables,
posteriormente se muestra un mensaje por pantalla con los elementos de la tupla usando
las variables individuales declaradas."""

persona = ("Manuel", "22", "Sevilla")
nombre, edad, ciudad = persona

print(f"Nombre -> {nombre} \nEdad -> {edad} \nCiudad -> {ciudad} ")