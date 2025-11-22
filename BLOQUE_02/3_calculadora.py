"""
Crea un script que contenga 4 funciones separadas:
 · sumar(a, b) → devuelve la suma.
 · restar(a, b) → devuelve la resta.
 · multiplicar(a, b) → devuelve la multiplicación.
 · dividir(a, b) → devuelve la división (controlando la división por cero).

El programa principal debe:
1. Pedir dos números al usuario.
2. Llamar a cada función y mostrar los resultados.
3. Incluir un docstring explicativo en cada función.
4. Cumplir las normas de estilo PEP 8.
"""

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