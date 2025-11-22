"""
Crea un script que:
1. Defina una variable global contador = 0.
2. Implemente tres funciones:
 · incrementar() → suma 1 al contador.
 · decrementar() → resta 1 al contador.
 · mostrar_contador() → imprime el valor actual.
3. Use la palabra clave global para modificar el contador dentro de las funciones.
4. Desde el programa principal, llama a las funciones en este orden:
 · incrementar() dos veces.
 · decrementar() una vez.
 · mostrar_contador().
5. Añade un docstring en cada función explicando lo que hace.
"""

contador = 0

def incrementar():
    """Incrementa el valor de la variable global "contador" en 1."""
    global contador
    contador += 1

def decrementar():
    """Decrementa el valor de la variable global "contador" en 1."""
    global contador
    contador -= 1

def mostrar_contador():
    """Muestra el valor actuañ de la variable global "contador"."""
    global contador
    print(f" Valor actual de contador -> {contador}")

incrementar() # Contador +1 (contador = 1)
incrementar() # Contador +1 (contador = 2)
decrementar() # Contador -1 (contador = 1)
mostrar_contador() # Imprime valor actual del contador (contador = 1)