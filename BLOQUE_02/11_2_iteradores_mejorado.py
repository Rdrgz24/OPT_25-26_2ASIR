"""Ejercicio con iteradores - Programa que en base a unos estudiantes con nota de tres materias
muestra por pantalla dichas notas, el promedio de ellas y el estado (aprobado, recuperación
o suspenso). Varios problemas como KeyError y Stop Iteration solventados."""

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
        # Mostrar por pantalla claves y valores recogidos
        print(f"{estudiante} - Notas: {notas}, Promedio de notas: {promedio}, Estado: {estado}")
    else:
        break