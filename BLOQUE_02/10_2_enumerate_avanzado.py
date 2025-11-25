"""Haciendo uso de enumerate() y zip() mostrar un indice, nombre del estudiante, notas, promedio
y estado de la calificación final. Con zip juntamos los elementos de las listas y con enumerate
añadimos un indice a cada uno de los elementos del iterable.
Por mera curiosidad, si añades cualquier otro campo en la lista sin estar completo en el resto,
comprobé que no se añade ni se muestra, debe cumplir en todas las listas."""

estudiantes = ["Carlos", "Teo", "Pablo", "Daniel", "Pepe"]
notas_matematicas = [5, 4, 7, 10]
notas_fisica = [4, 6, 8, 8]
notas_quimica = [9, 7, 6, 9]

# Bucle donde "i" es el indice y est, mat, fis y qui son los datos de las tablas que juntamos con zip, empezamos por 1.
for i, (est, mat, fis, qui) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):
    # Calcular promedio y hacer condiciones.
    promedio = (mat + fis + qui) / 3
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"
    # Mostrar valores por pantalla.
    print(f"{i} {est} - Matemáticas: {mat}, Física: {fis}, Química: {qui} ")