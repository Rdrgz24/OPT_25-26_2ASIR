estudiantes = ["Paco", "Javier", "Rodrigo", "Hugo"]
notas_mates = [7, 6, 6, 5]
notas_fisica = [6, 5, 10, 7]
notas_quimica = [6, 3, 5, 10]

resultado_final = {}

for nom, mat, fis, qui in zip(estudiantes, notas_mates, notas_fisica, notas_quimica):
    promedio = round((mat + fis + qui) / 3, 2)
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    elif promedio < 5:
        estado = "Reprobado"
    else:
        estado = "Nota no válida"

    resultado_final[nom] = {
        "Matemáticas": mat,
        "Física": fis,
        "Química": qui,
        "Promedio": promedio,
        "Estado": estado
    }

for clave, valores in resultado_final.items():
    print(f"Nombre: {clave} - "
          f"Matemáticas: {valores['Matemáticas']}, "
          f"Física: {valores['Física']}, "
          f"Química: {valores['Química']}, "
          f"Promedio de notas: {valores['Promedio']}, "
          f"Estado: {valores['Estado']}")