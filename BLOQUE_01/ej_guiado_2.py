# Ejercicio guiado 2 - No evaluable

#Crea un script que:
# 1. Guarde en variables tu nombre, edad, altura y si estás estudiando (True/False).
# 2. Muestre en pantalla un mensaje como:
# Me llamo Carla, tengo 19 años, mido 1.68 y actualmente estudio: True

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuál es tu edad? "))
altura = float(input("¿Cuánto mides en cm? ")) / 100

# Recoge un texto con input() (True, true, TRUE; False, false, FALSE; y lo convierte a minúscula con .lower())
# Luego hace la comparativa y es cuando se vuelve en booleano =
# true == true -> True (propio valor booleano)
# false == true -> False (propio valor booleano)
# Cualquier otro valor introducido será false.
estudio = input("¿Estudias? True/False -> ").lower() == "true"

print(f"Me llamo {nombre}, tengo {edad} años, mido {altura} y actualmente estudio: {estudio}")