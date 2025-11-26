"""El programa crea una tupla con tres elementos y la desempaqueta en tres variables,
posteriormente se muestra un mensaje por pantalla con los elementos de la tupla usando
las variables individuales declaradas."""

# Crear la tupla
persona = ("Manuel", "22", "Sevilla")
nombre, edad, ciudad = persona # Desempaquetarla en variables nombre, edad, ciudad
# Mostrar elementos por pantalla.
print(f"Nombre -> {nombre} \nEdad -> {edad} \nCiudad -> {ciudad} ")