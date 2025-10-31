"""
Crea un script que:
1. Pida al usuario tres notas.
2. Calcule el promedio.
3. Introduzca un error lógico en el cálculo (como en el ejemplo anterior).
4. Usa IntelliJ en modo depuración para encontrar y corregir el error.
5. Añade un docstring al inicio explicando qué hacía mal el programa y cómo se corrigió.
"""
"""
Docstring explicando el mal funcionamiento del programa y corrección:

Connected to: <socket.socket fd=740, family=2, type=1,
proto=0, laddr=('127.0.0.1', 60705),
raddr=('127.0.0.1', 60704)>.
Connected to pydev debugger (build 252.26199.169)
Introduce la nota 1 -> 4
Introduce la nota 2 -> 5
Introduce la nota 3 -> 6
El promedio es 11.0 <--- Línea importante (ERROR)

El promedio de 4 + 5 + 6 = 5, el problema está en que
la siguiente línea de código está mal definida:
promedio = nota_1 + nota_2 + nota_3 / 3
Para corregirla debemos usar la precedencia de operadores:
promedio = (nota_1 + nota_2 + nota_3) / 3
"""
nota_1 = float(input("Introduce la nota 1 -> "))
nota_2 = float(input("Introduce la nota 2 -> "))
nota_3 = float(input("Introduce la nota 3 -> "))

promedio = (nota_1 + nota_2 + nota_3) / 3
print(f"El promedio es {promedio}")