# Crea un script que:
# 1. Pida al usuario dos números (num1, num2).
# 2. Pida elegir una operación: suma, resta, multiplicación o división.
# 3. Use if...elif...else para realizar la operación seleccionada.
# 4. Si elige una opción inválida, mostrar "Operación no reconocida".
# 👉 Ejemplo de salida:
#   Elige operación (suma, resta, multiplicacion, division): suma
#   Resultado: 25

num1 = float(input("Escribe el número 1 -> "))
num2 = float(input("Escribe el número 2 -> "))
# Utilizamos .lower() para que el usuario pueda introducir mayúscula o minúscula y la condición lo interprete de
# igual manera.
operacion = input("Escribe operación: Suma, Resta, Multiplicacion o Division -> ").lower()

if operacion == "suma":
    print(f"La suma de {num1} y {num2} es {num1 + num2}")
elif operacion == "resta":
    print(f"La resta de {num1} y {num2} es {num1 - num2}")
elif operacion in ["multiplicacion", "multiplicación"]:
    print(f"La multiplicación de {num1} y {num2} es {round(num1 * num2, 2)}")
elif operacion in ["division", "división"]:
    if num2 != 0:
        print(f"La división de {num1} y {num2} es {round(num1 / num2, 2)}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Operación no reconocida")

# https://es.stackoverflow.com/questions/448129/c%C3%B3mo-puedo-quitar-los-acentos-en-python