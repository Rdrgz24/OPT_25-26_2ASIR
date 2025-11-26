"""Este programa define 4 funciones (sumar, restar, multiplicar y dividir) el
usuario introduce los valores por teclado y se muestra por pantalla los
resultados de cada operación. (Segundo número de división no puede ser 0)"""

a = float(input("Introduce el primer número -> "))
b = float(input("Introduce el segundo número -> "))

def sumar(a, b):
    """Función que suma dos parámetros pasados por teclado (a y b)."""
    return a + b

def restar(a, b):
    """Función que resta dos parámetros pasados por teclado (a y b)."""
    return a - b

def multiplicar(a, b):
    """Función que multiplica dos parámetros pasados por teclado (a y b)."""
    return a * b

def dividir(a, b):
    """Función que divide dos parámetros pasados por teclado (a y b).
        Si el número = 0 no se puede dividir, de lo contrario se divide"""
    if b == 0:
        print("El segundo número no puede ser 0.")
    else:
        return a / b

print("\nLa suma es -> ", sumar(a, b))
print("La resta es -> ", restar(a, b))
print("La multiplicación es -> ", multiplicar(a, b))
# Para evitar que salga el mensaje "La división es -> None, hacemos una condición en base al resto.
res_div = dividir(a, b)
if res_div != None:
    print("La división es -> ", dividir(a, b))