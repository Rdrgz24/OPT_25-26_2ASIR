"""
1. Crea tres listas:
nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]
2. Usa zip() para imprimir:
Ana - Matemáticas: 8, Física: 9
Luis - Matemáticas: 7, Física: 6
Marta - Matemáticas: 9, Física: 10
--- Esto permitirá a los alumnos ver cómo combinar varias listas con zip() de forma práctica.
"""

nombres = ["Pepe", "Mateo", "Rubén"]
notas_mates = [10, 5, 7]
notas_fisica = [8, 8, 9]

for nom, mat, fis in zip(nombres, notas_mates, notas_fisica):
    print(f"{nom} - Nota de matemáticas -> {mat}, Nota de física -> {fis}")