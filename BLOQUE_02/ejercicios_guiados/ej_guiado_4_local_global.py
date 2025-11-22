"""
1. Define una variable global curso = "Python".
2. Crea una función mostrar_curso() que imprima la variable global.
3. Crea otra función cambiar_curso() que defina una variable local con el mismo nombre y muestre su valor.
4. Ejecuta ambas funciones y observa la diferencia.
"""

curso = "Python" # Declaramos la variable global "curso" con valor "Python"

def mostrar_curso():
    """Función que muestra por pantalla el valor actual de la variable global."""
    print(curso)

def cambiar_curso():
    """Función que cambia el valor de la variable global a local y lo muestra por pantalla."""
    curso = "Python_local" # Cambio de variable a local, dentro de esta función su valor es "Python_local"
    print(curso)

mostrar_curso() # Muestra valor de variable global
cambiar_curso() # Muestra valor de variable local dentro de esta función.
# Muestra el valor de la varible curso, como es de lógica mostrará "Python",
# simplemente es para demostrar que no se cambia el valor, solo dentro de la función."
print(curso)