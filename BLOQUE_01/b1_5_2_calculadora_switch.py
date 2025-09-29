# Crea un script que:
#
# 1. Pida al usuario dos números (num1, num2).
# 2. Pida elegir una operación: suma, resta, multiplicación o división.
# 3. Use match-case para realizar la operación seleccionada.
# 4. Si elige una opción inválida, mostrar "Operación no reconocida".
# 👉 Ejemplo de salida:
# Elige operación (suma, resta, multiplicacion, division): multiplicacion
# Resultado: 50

num1 = float(input("Escribe el número 1 -> "))
num2 = float(input("Escribe el número 2 -> "))
# Usamos .lower() para convertir el texto en minúscula y sea más fácil de comparar en el match-case.
operacion = input("Escribe operación: Suma, Resta, Multiplicacion o Division -> ").lower()

match operacion:
    case "suma":
        print(f"La suma de {num1} y {num2} es {num1 + num2}")
    case "resta":
        print(f"La resta de {num1} y {num2} es {num1 - num2}")
    case "multiplicacion" | "multiplicación":
        print(f"La multiplicación de {num1} y {num2} es {round(num1 * num2, 2)}")
    case "division" | "división":
        if num2 != 0:
            print(f"La división de {num1} y {num2} es {round(num1 / num2, 2)}")
        else:
            print("No se puede dividir entre cero.")
    case _:
        print("Operación no reconocida.")