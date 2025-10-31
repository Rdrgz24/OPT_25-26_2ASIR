"""
Crea un script que:
1. Defina una lista con al menos 6 nombres.
2. Recorra la lista con un bucle for.
3. Use continue para saltar los nombres que empiezan por la letra "A" (mayúscula o minúscula).
4. Muestre en pantalla solo los nombres que no empiecen por "A".
5. Añada un docstring explicando el propósito del programa y comentarios en las partes importantes del código.
 · Ejemplo de entrada/salida:
lista = ["Ana", "Pedro", "Alba", "Lucía"]
 · Resultado:
Pedro
Lucía
"""
# Definimos la lista (mínimo de 6 nombres)
lista = ["José", "Alba", "Almudena", "Santiago", "Yolanda", "Adrián"]

# Bucle for que recorre cada nombre de la lista.
for nombre in lista:
    # Si encuentra una "A" mayúscula se convierte en "a" minúscula gracias a .lower()
    # Gracias a .startswith() filtramos por la palabra que empieza en cada nombre.
    if nombre.lower().startswith("a"):
        # Si empieza por "A" o "a" continua el bucle for.
        continue
    # Si no empieza por "A" o "a" muestra el nombre en cuestión por pantalla.
    print(nombre)