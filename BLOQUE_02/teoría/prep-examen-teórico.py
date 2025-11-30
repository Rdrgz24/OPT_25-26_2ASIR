# Unidad 2.1 – Funciones: definición

"""
Una función es un bloque de código que se define una vez y permite ejecutarla varias veces
 · Dentro de sus características principales:
Definición única -> Se escribe una vez -> Se utiliza muchas
Parámetros (opcionales) -> datos que se reciben para trabajar con ellos
Valor de retorno (opcional) -> Resultado que entrega tras ejecutarse (normalmente el valor se devuelve con return, ya que print = None)
Reutilización -> Puedes invocarla desde cualquier parte del programa.
 · Es por ello, que tenemos las ventajas...
Reutilizar código sin repetir instrucciones
Organizar y trabajar limpio
Facilitar mantenimiento (errores más localizables)
Permite colaborar en equipo (un programador -> "x" nº de funciones)
Modularidad -> Dividir un programa en pequeñas partes.
"""
def nombre_de_la_funcion(): #def -> define funcion. nombre -> descriptivo. () -> pasar parámetros (opcional). : -> inicio bloque.
    # La identación es obligatoria (4 espacios por nivel)
        # Nivel 2
            # Nivel 3
    """
    Docstring: Explica lo que hace la función.
    """
    # bloque de instrucciones

def saludar():
    """Muestra un saludo en pantalla."""
    print("¡Hola! Bienvenido a Python.")

# Llamada a la función
saludar()

# Unidad 2.2 – Funciones con parámetros

"""
Lo lógico es que las funciones trabajen con información que recibe del exterior:
 · Parámetros -> Variables dentro de la función que reciben datos.
 · Argumentos -> Valor real que se pasa cuando llamas a la función.
"""
# Ejemplo simple
def saludar(nombre): # Nombre es el parámetro.
    """Muestra un saludo usando un nombre recibido como parámetro."""
    print(f"Hola {nombre}!")

saludar("Ana") # El valor "Ana" es el argumento.

# Tipos de parámetros
# 1. Posicionales -> Mismo orden en el que se definieron

def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años.")

saludar("Ana", 20)  # nombre="Ana", edad=20

# 2. Con valor por defecto -> Si no pasas el argumento, tiene un valor predeterminado.

def bienvenida(nombre, curso="Python"):
    """Muestra un mensaje de bienvenida al curso."""
    print(f"Bienvenido {nombre} al curso de {curso}.")

bienvenida("Ana")           # usa "Python" por defecto
bienvenida("Pedro", "Java") # sobrescribe el curso

# 3. Con argumentos nombrados (distinto orden)

def mostrar_persona(nombre, edad, profesion):
    """Muestra los datos básicos de una persona."""
    print(f"Nombre: {nombre}, Edad: {edad}, Profesión: {profesion}")

# Los nombre de los parámetros se indican al llamar la función y permiten cambiar el orden.
mostrar_persona("Laura", 25, "Ingeniera")   # posicionales
mostrar_persona(edad=40, profesion="Doctor", nombre="José")  # nombrados

# Buenas prácticas con parámetros:
# 1. Usar nombres descriptivos.
# 2. Si función tiene muchos parámetros -> Recomendable usar argumentos nombrados.
# 3. Evitar usar valores por defecto que sean listas o diccionarios (pueden provocar error).

# Unidad 2.3 – Funciones con valores de retorno

"""
Funciones con print -> No tienen valor. Lo útil en programación es que se devuelvan valores.
 · return -> finaliza le ejecución de la función y devuelve el resultado donde fue llamada.
 · Si no hay return -> Devuelve None.
 · Función debe estar diseñada para:
    · Resolver una sola tarea.
    · Devolver un único resultado principal.
Resumen, print() solo muestra por pantalla y return entrega el valor. 
"""

# Ejemplo 1 - Función que devuelve un valor

def cuadrado(numero):
    """Devuelve el cuadrado de un número."""
    return numero ** 2

resultado = cuadrado(5)
print("El cuadrado es:", resultado)

# Ejemplo 2 - Función que no devuelve un nada

def mostrar_mensaje():
    """Muestra un mensaje en pantalla, pero no devuelve nada."""
    print("Hola, soy una función sin return.")

respuesta = mostrar_mensaje()
print("El valor devuelto es:", respuesta)  # None

# Ejemplo 3 - Combinando funciones con return

def doble(n):
    """Devuelve el doble de un número."""
    return n * 2

def triple(n):
    """Devuelve el triple de un número."""
    return n * 3

numero = 4
print("El doble es:", doble(numero))
print("El triple es:", triple(numero))

# Buenas prácticas al usar return:
# 1. Evitar usar print() para usar el resultado en cálculos posteriores.
# 2. Una función puede tener varios returm, pero es mejor tener un único punto de salida.
# 3. Usar docstrings claros que expliquen lo que devuelve la función.

# Unidad 2.4 – Funciones y ámbito (scope de variables)

"""
Scope (ámbito) define dónde una variable es visible y puede usarse.
Existen dos tipos:
1. Variable local: 
 · Se declara dentro de una función.
 · Solo existe cuando la función se ejecuta.
 · No es manipulable fuera de la función.
2. Variable global:
 · Se declara fuera de cualquier función.
 · Es accesible desde cualquier parte del programa.
3. Palabra "global" - reservada:
 · Permite modificar una variable global desde dentro de una función.
 · Se recomienda no abusar de ella, ya que puede volver difícil el código de mantener y depurar.
"""

def funcion():
    mensaje = "Hola desde la función"  # variable local
    print(mensaje)

funcion()
print(mensaje)  # ❌ Error: 'mensaje' no está definida

saludo = "Hola desde fuera"  # variable global

def mostrar_saludo():
    print(saludo)  # puede acceder a la variable global

mostrar_saludo()

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1

# Buenas prácticas:
# 1. Usar variables locales siempre que sea posible.
# 2. Evitar modificar variables globales desde funciones.
# 3. Pasar variables como parámetros y devolver valores en lugar de depender de globales.

# Unidad 2.5 – Listas

"""
Una lista en python es una colección ordenada (1, 2, 3...)y mutable (... 4, 5, 6) de elementos.
 · Se definen con corchetes lista = []
 · Pueden contener distintos tipos de datos (int, str...)
 · Van en orden, cada elemento tiene una posición.
 · Son mutables, se pueden añadir, eliminar, modificar los elementos tras crearse.
 · Soportan concatenación, repetición y pertenencia.

Podemos manipular listas con los métodos principales:
 · append(x) -> añade elemento al final
 · insert(i, x) -> inserta en una posición concreta
 · extend(lista) -> añade elementos de otra lista
 · remove(x) -> elimina la primera ocurrencia de un valor
 · pop(i) -> elimina el elemento de esa posición, si no se indica es el último
 · clear() -> vacía la lista
 · index(x) -> devuelve la posición del valor "x"
 · count(x) -> cuenta cuantas veces aparece el valor "x"
 · sort() -> ordena la lista (ascendente por defecto)
 · reverse() -> invierte el orden de los elementos
 · copy() -> realiza una copia de la lista
 · + -> concatena listas
 · * -> repite listas
 · in -> verifica pertenencia de un elemento
"""

numeros = [1, 2, 3, 4, 5]       # lista de enteros
mixta = ["Ana", 20, True, 3.5]  # mezcla de tipos
vacia = []                      # lista vacía

frutas = ["manzana", "pera", "plátano"]
print(frutas[0])    # manzana (primer elemento)
print(frutas[-1])   # plátano (último elemento)

frutas[1] = "naranja"   # cambia "pera" por "naranja"
print(frutas)           # ['manzana', 'naranja', 'plátano']

# Añadir y eliminar

numeros = [10, 20, 30]
numeros.append(40)
print(numeros)   # [10, 20, 30, 40]

numeros.pop(1)   # elimina el elemento en posición 1
print(numeros)   # [10, 30, 40]

# Ordenar y buscar

edades = [18, 25, 20, 22]
edades.sort()
print(edades)           # [18, 20, 22, 25]
print(edades.index(20)) # posición 1

# Copiar listas (copia vs referencia)

lista1 = [1, 2, 3]
lista2 = lista1          # referencia, apuntan a lo mismo
lista3 = lista1.copy()   # copia independiente

lista2.append(4)
print(lista1)  # [1, 2, 3, 4]
print(lista3)  # [1, 2, 3]

# Pertenencia y concatenación

frutas = ["manzana", "pera", "plátano"]

print("pera" in frutas)       # True
print("uva" not in frutas)    # True

otras_frutas = ["sandía", "kiwi"]
todas = frutas + otras_frutas
print(todas)  # ['manzana', 'pera', 'plátano', 'sandía', 'kiwi']