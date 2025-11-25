"""
1. Crea una lista de números del 1 al 5.
2. Convierte la lista en un iterador.
3. Imprime cada elemento usando next() dentro de un while.
"""

numeros = [1, 2, 3, 4, 5]
iterable = iter(numeros)

valor = next(iterable, None)
while valor is not None:
    print(valor)
    valor = next(iterable, None)