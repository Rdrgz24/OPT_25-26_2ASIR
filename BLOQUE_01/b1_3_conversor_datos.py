#Crea un script que:
#1. Pida al usuario por teclado su nombre, edad y altura (usa input() para capturar los datos).
#2. Convierte la edad a int y la altura a float.
#3. Muestra un mensaje en pantalla como:
#Hola, me llamo Ana, tengo 30 años y mido 1.65 metros.

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
altura= input("¿Cuánto mides en cm? ")
# Se convierten las variables a int y float ya que los datos que se recogen en el input() se guardan como cadena de texto (str)
edad = int(edad)
altura = float(altura) / 100

print(f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura} metros.")