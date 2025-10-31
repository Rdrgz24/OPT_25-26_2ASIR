"""
1. Define una función area_rectangulo(base, altura) que devuelva el área del rectángulo.
2. Define una función perimetro_rectangulo(base, altura) que devuelva el perímetro.
3. Desde el programa principal, pide al usuario la base y la altura, y muestra:
 · El área calculada.
 · El perímetro calculado.
Objetivo: practicar funciones con un solo resultado devuelto.
"""
b = float(input("Introduce la base del rectángulo -> "))
a = float(input("Introduce la altura del rectángulo -> "))

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

print("El área del rectángulo es ", area_rectangulo(b, a))
print("El perímetro del rectángulo es ", perimetro_rectangulo(b, a))