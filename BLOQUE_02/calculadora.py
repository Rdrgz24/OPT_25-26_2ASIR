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

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("El segundo número no puede ser 0.")
    else:
        return a / b

a = float(input("Introduce el primer número -> "))
b = float(input("Introduce el segundo número -> ",))

print("\nLa suma es -> ", sumar(a, b))
print("La resta es -> ", restar(a, b))
print("La multiplicación es -> ", multiplicar(a, b))
res_div = dividir(a, b)
if res_div != None:
    print("La división es -> ", dividir(a, b))