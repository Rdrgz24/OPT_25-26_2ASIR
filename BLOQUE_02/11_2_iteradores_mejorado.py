"""
1. Tenemos un diccionario con estudiantes y sus notas en tres materias:
estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}
2. Crea un iterador sobre las claves del diccionario.
3. Recorre el iterador usando next() dentro de un while True.
4. Para cada estudiante:
· Calcula el promedio de sus notas.
· Determina el estado:
  · "Aprobado" si promedio ≥ 6.5
  · "En recuperación" si promedio ≥ 5 y < 6.5
  · "Reprobado" si promedio < 5
5. Imprime un reporte claro y ordenado:
Ana - Notas: [8, 7, 9], Promedio: 8.0, Estado: Aprobado
Luis - Notas: [7, 6, 8], Promedio: 7.0, Estado: Aprobado
Marta - Notas: [9, 10, 9], Promedio: 9.33, Estado: Aprobado
Carlos - Notas: [6, 7, 5], Promedio: 6.0, Estado: En recuperación
Laura - Notas: [10, 9, 10], Promedio: 9.67, Estado: Aprobado
"""

estudiantes = {
    "Ana": [6, 6, 5],
    "Luis": [3, 6, 4],
    "Marta": [9, 4, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 4, 10]
}
# Creamos el iterador en base a la lista de estudiantes
iterador = iter(estudiantes)
while True:
    # Recorremos las claves del diccionario con next()
    estudiante = next(iterador, None) # KeyError: None -> Me hizo saber que debía poner ", None"
    if estudiante is not None: # Me dió error "StopIteration" al no detectar más claves, aplico condición y no vuelve a pasar.
        notas = estudiantes[estudiante] # Extraer valores en base a cada estudiante.
        promedio = round(sum(notas) / len(notas), 2) # Calcular promedio - sumar notas y dividir entre el total que haya.
        # Condiciones de aprobado, recuperación o suspenso.
        # ¿Sería útil añadir otro elif para < 5 y el último else: "Nota no válida"? -> Preguntar a Javi
        if promedio >= 6.5:
            estado = "Aprobado"
        elif promedio >= 5:
            estado = "En recuperación"
        else:
            estado = "Reprobado"
        print(f"{estudiante} - Notas: {notas}, Promedio de notas: {promedio}, Estado: {estado}")
    else:
        break