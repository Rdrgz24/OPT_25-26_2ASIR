""" Crear tres listas y juntar sus valores con zip() para posteriormente imprimirlo.
zip() junta primer valor de una lista con primer valor de la otra, y así sucesivamente."""

nombres = ["Pepe", "Mateo", "Rubén"]
notas_mates = [10, 5, 7]
notas_fisica = [8, 8, 9]

for nom, mat, fis in zip(nombres, notas_mates, notas_fisica):
    print(f"{nom} - Nota de matemáticas -> {mat}, Nota de física -> {fis}")