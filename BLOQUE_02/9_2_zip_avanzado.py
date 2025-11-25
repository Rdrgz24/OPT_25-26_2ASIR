"""En base a listas juntadas con zip y un diccionario vacío, asignar clave y valor a dicho
diccionario con los valores recogidos en las listas"""

# Declarar las listas de estudiantes y sus notas
estudiantes = ["Paco", "Javier", "Rodrigo", "Hugo"]
notas_mates = [7, 6, 6, 5]
notas_fisica = [6, 5, 10, 7]
notas_quimica = [6, 3, 5, 10]

# Declarar diccionario vacio
resultado_final = {}

# Bucle con zip que recoge todos los datos de las listas y los junta
for nom, mat, fis, qui in zip(estudiantes, notas_mates, notas_fisica, notas_quimica):
    # Declarar variable promedio y condiciones en base a dicha media (aprobado, recu o suspenso)
    promedio = round((mat + fis + qui) / 3, 2)
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"
    # Insertamos valores recogidos con zip en el diccionario
    # resultado_final[nom] usará el nombre como clave y el resto de datos como valores.
    resultado_final[nom] = {
        "Matemáticas": mat,
        "Física": fis,
        "Química": qui,
        "Promedio": promedio,
        "Estado": estado
    }

# Bucle for para recorrer los items del diccionario y mostrarlos por pantalla.
for clave, valores in resultado_final.items():
    print(f"Nombre: {clave} - "
          f"Matemáticas: {valores['Matemáticas']}, "
          f"Física: {valores['Física']}, "
          f"Química: {valores['Química']}, "
          f"Promedio de notas: {valores['Promedio']}, "
          f"Estado: {valores['Estado']}")