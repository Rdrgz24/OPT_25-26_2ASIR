"""
1. Se tienen tres listas:
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
2. Recorre las listas simultáneamente usando enumerate() y zip().
 · El índice debe empezar en 1.
3. Para cada estudiante, calcula:
 · Promedio de sus notas.
 · Calificación final según el promedio:
   · "Aprobado" si promedio ≥ 6.5
   · "En recuperación" si promedio ≥ 5 y < 6.5
   · "Reprobado" si promedio < 5
4. Muestra un reporte en pantalla con el índice, nombre del estudiante, notas, promedio y calificación final.
"""

estudiantes = ["Carlos", "Teo", "Pablo", "Daniel"]
notas_matematicas = [5, 4, 7, 10]
notas_fisica = [4, 6, 8, 8]
notas_quimica = [9, 7, 6, 9]

for i, (est, mat, fis, qui) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):
    promedio = (mat + fis + qui) / 3
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    elif promedio < 5:
        estado = "Reprobado"
    else:
        estado = "Nota no válida"

    print(f"{i} {est} - Matemáticas: {mat}, Física: {fis}, Química: {qui} ")