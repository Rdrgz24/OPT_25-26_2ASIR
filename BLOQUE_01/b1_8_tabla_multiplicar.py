"""
Script que pide un número cualquiera al usuario,
usa un bucle for para mostrar su tabla de
multiplicar del 1 al 10.
"""
# Pide al usuario introducir un número, se define
# se convierte de str a float, ya que los datos
# que salen del input son str.
# Se usa float para dar mas posibilidades en la
# calculadora.
num = float(input("Introduce un número -> "))

print(f"Tabla de multiplicar del {num}")
# Bucle del 1 al 11, cuando llega a 11 para
# y no lo muestra por pantalla.
for i in range(1, 11):
    # Imprime el número junto al valor actual de i,
    # formando así la tabla de multiplciar completa.
    print(f"{num} x {i} = {num * i}")