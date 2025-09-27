# Ejercicio guiado 4 - No evaluable

# Crea un script clasificador_edad.py que:
# Pida al usuario su edad.
# Use condicionales para mostrar:
# -> "Eres menor de edad" si es < 18.
# -> "Eres adulto" si está entre 18 y 65.
# -> "Eres adulto mayor" si es >= 65.

edad = int(input("Introduce tu edad -> "))

if edad >= 65:
    print("Eres adulto mayor")
elif edad >= 18:
    print("Eres adulto")
else:
    print("Eres menor de edad")