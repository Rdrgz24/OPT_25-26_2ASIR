"""El programa incorpora una variable global "contador" que empieza en 0, hay
tres funciones, una incrementa el contador, otra lo decrementa y la última
muestra el valor actual de la variable global "contador" por pantalla."""

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
    print(f"Valor actual de contador -> {contador}")

incrementar() # Contador +1 (contador = 1)
incrementar() # Contador +1 (contador = 2)
decrementar() # Contador -1 (contador = 1)
mostrar_contador() # Imprime valor actual del contador (contador = 1)