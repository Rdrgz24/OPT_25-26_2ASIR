#Crea un script que:
# -> Tenga dos variables num1 y num2.
# -> Calcule y muestre: suma, resta, multiplicación, división, módulo y potencia.

num1 = float(input("Escribe el número 1-> "))
num2 = float(input("Escribe el número 2-> "))

if num1 == 0 or num2 == 0:
    print("Ningun número puede ser 0")
else:
    print(f"\nLa suma de {num1} y {num2} es {num1 + num2}")
    print(f"La resta de {num1} y {num2} es {num1 - num2}")
    print(f"La multiplicación de {num1} y {num2} es {num1 * num2}")
    print(f"La división de {num1} y {num2} es {num1 / num2}")
    print(f"El módulo o resto de {num1} y {num2} es {num1 % num2}")
    print(f"La potencia de {num1} y {num2} es {num1 ** num2}")