"""
1. Crea dos listas:
 · numeros = [1, 2, 3]
 · letras = ["A", "B", "C"]
2. Usa zip() para recorrer ambas listas y mostrar:
Número 1 - Letra A
Número 2 - Letra B
Número 3 - Letra C
"""

numeros = [1, 2, 3]
letras = ["A", "B", "C"]

for num, let in zip(numeros, letras):
    print(f"Número {num} --- Letra {let}")