"""
Crea dos listas:
numeros = [1, 2, 3]
letras = ["A", "B", "C"]
Usa zip() para recorrer ambas listas y mostrar:
Número 1 - Letra A
Número 2 - Letra B
Número 3 - Letra C
"""


numeros = [1, 2, 3]
letras = ["A", "B", "C"]

resultado = zip(numeros, letras)
print(list(resultado))