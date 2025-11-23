"""
1. Define una tupla con los 7 días de la semana.
2. Muestra el primer y el último día.
3. Recorre la tupla con un bucle for para mostrar todos los días.
4. Usa index() para encontrar en qué posición está el día "Miércoles".
"""

dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

print(f"Primer día -> {dias[0]}")
print(f"Primer día -> {dias[-1]}")
print("Bucle for")
for d in dias:
    print(d)

print(f"El miércoles está en la posición {dias.index("miércoles")}")

dia = input("Introduce el día (con tilde) -> ")

def posicion(dia):
    """Función que devuelve la posición de un día pasado por parámetro.
    Se pasa en minúsculas para normalizar el parámetro que pasa el usuario."""
    dias_min = dia.lower()
    if dias_min in dias:
        print(f"El día {dias_min} está en la posición {dias.index(dias_min)}")
    else:
        print(f"{dias_min} no está en la tupla.")

posicion(dia)
