# Crea un script que:
# 1. Pida un número al usuario.
# 2. Use un bucle while para contar desde ese número hasta 0.
# · Al final muestre: "¡Despegue!".
# 👉 Ejemplo de salida:
# Introduce un número: 5
# 5
# 4
# 3
# 2
# 1
# 0
# ¡Despegue!

num = int(input("Introduce un número -> "))

if num < 0:
    print("El número no puede ser menor que 0")
else:
    while num != -1:
        print(num)
        num -= 1
    print("¡Despegué!")