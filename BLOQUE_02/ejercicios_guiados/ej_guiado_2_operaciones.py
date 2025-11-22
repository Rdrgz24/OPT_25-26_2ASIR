"""
1. Define una función sumar(a, b) que imprima la suma de dos números.
2. Define una función saludo_personal(nombre, saludo="Hola") que muestre un saludo personalizado.
3. Llama a ambas funciones con distintos parámetros desde el programa principal.
"""

def sumar(a, b):
    """Define una función con dos argumentos y los suma."""
    print(f"Suma de {a} + {b} = {a + b}")

def saludo_personal(nombre, saludo="Hola"):
    """Define una función con dos argumentos y saluda en base a un nombre."""
    print(f"{saludo} {nombre}, encantado de conocerte.")

# Sumando números
sumar(8, 12)
sumar(b=20, a=40)
# Sin segundo argumento (usa el que viene por defecto)
saludo_personal("Rafael")
# Con segundo argumento
saludo_personal("Marcos", "Que pasa")
# Con parámetros pero puestos al revés
saludo_personal(saludo="Buenas tardes", nombre="Mario")