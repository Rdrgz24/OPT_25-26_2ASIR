"""
1. Define una tupla con los 7 días de la semana.
2. Muestra el primer y el último día.
3. Recorre la tupla con un bucle for para mostrar todos los días.
4. Usa index() para encontrar en qué posición está el día "Miércoles".
"""

dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domigo")

print(f"Primer día -> {dias[0]}")
print(f"Primer día -> {dias[-1]}")
print("Bucle for")
for d in dias:
    print(d)

dia = input("Introduce el día -> ")


def posicion(dia):
    if dia in dias:
        print(f"El día {dia} está en la posición {dias.index(dia)}")
    else:
        print(f"{dia} no está en la tupla.")

posicion(dia)
