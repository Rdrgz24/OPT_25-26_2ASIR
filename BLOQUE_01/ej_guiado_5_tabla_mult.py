# Crea un script tabla_multiplicar.py que:
# 1. Pida un número al usuario.
# 2. Use un bucle for para mostrar su tabla de multiplicar del 1 al 10.
# 👉 Ejemplo de ejecución:
# Introduce un número: 7
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

num = int(input("Introduce un número -> "))
i = 1

print(f"Tabla de multiplicar del {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")