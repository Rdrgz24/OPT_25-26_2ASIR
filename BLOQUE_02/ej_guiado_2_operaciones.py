"""
Define una función sumar(a, b) que imprima la suma de dos números.
Define una función saludo_personal(nombre, saludo="Hola") que muestre un saludo personalizado.
Llama a ambas funciones con distintos parámetros desde el programa principal.
"""

def sumar(a, b):
    print(f"{a + b}")

def saludo_personal(nombre, saludo="Hola"):
    print(f"{saludo} {nombre}, encantado de conocerte.")

sumar(8, 12)
# Sin segundo argumento (usa el que viene por defecto)
saludo_personal("Rafael")
# Con segundo argumento
saludo_personal("Marcos", "Que pasa")