"""
1. Define una variable global curso = "Python".
2. Crea una función mostrar_curso() que imprima la variable global.
3. Crea otra función cambiar_curso() que defina una variable local con el mismo nombre y muestre su valor.
4. Ejecuta ambas funciones y observa la diferencia.
"""
curso = "Python"

def mostrar_curso():
    print(curso)

def cambiar_curso():
    curso = "Local"
    print(curso)

mostrar_curso()
cambiar_curso()