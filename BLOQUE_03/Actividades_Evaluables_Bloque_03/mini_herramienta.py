"""Menú principal Al iniciar, el programa debe mostrar:

--- Menú de Herramientas ---
1. Cálculos matemáticos
2. Explorador de directorios
3. Consulta a API (requests)
4. Salir
El usuario podrá elegir una opción escribiendo un número.

Opción 1 – Cálculos matemáticos (math)

Pedir un número entero al usuario.

Mostrar en pantalla:

Su raíz cuadrada.
Su factorial.
Su potencia al cuadrado.
Opción 2 – Explorador de directorios (os)

Mostrar el directorio actual.

Listar todos los archivos y carpetas de esa ruta.

Preguntar al usuario si quiere crear una nueva carpeta:

Si responde “sí”, pedir el nombre y crearla con os.mkdir().
Si responde “no”, volver al menú.
Opción 3 – Consulta a API (requests)

Hacer una petición GET a la URL fija:

https://api.github.com
Mostrar en pantalla:

El código de estado (status_code).
El tamaño de la respuesta en caracteres (len(respuesta.text)).
Los primeros 200 caracteres del contenido (respuesta.text[:200]).
Manejar errores con try/except para evitar que el programa se rompa si no hay conexión.

Opción 4 – Salir

Finalizar el programa mostrando un mensaje de despedida.
"""

import math
import os
import requests

def calc_mat():
    """Calcula la raíz cuadrada, factorial y potencia al cuadrado en base al número que inserta el usuario."""
    try:
        numero = int(input("Inserta un número entero -> ")) # Pide entero al usuario
        print("\nRaíz cuadrada:", math.sqrt(numero)) # Calcula raiz cuadrada
        print("Factorial:", math.factorial(numero)) # Calcula factorial
        print("Potencia al cuadrado:", math.pow(numero, 2)) # Calcula potencia al cuadrado (elevado 2)
    except ValueError:
        print("El valor ingresado no es entero.")

def os_exp():
    """Muestra el directorio actual, sus archivos y da la posibilidad de crear un nuevo directorio dentro de este.
    Además, añadí la funcionalidad para que, tras añadir el directorio, recorra todos los que
    están disponibles dentro."""
    try: # Intento...
        print("Directorio actual:", os.getcwd()) # Muestra directorio actual donde ejecutas la herramienta.
        print("Archivos en la carpeta:")
        archivos = os.listdir(".") # Creo variable que guarde todos los archivos
        for archivo in archivos: # Recorre cada uno de los archivos y directorios
            if os.path.isfile(archivo): # Filtra por archivo
                print(archivo) # Los muestra por pantalla.
        resp = input("¿Quieres crear una nueva carpeta? (si / no)-> ") # Pregunta al usuario de añadir directorio.
        if resp.lower() in ("si", "sí"): # Filtrar la respuesta siempre por minúscula y con tilde.
            fold_name = input("Introduce el nombre para la carpeta -> ")
            os.mkdir(fold_name) # Crea la carpeta.
            print("Carpetas actuales en el directorio actual tras la creación:")
            dirs = os.listdir(".") # Variable para guardar tanto ficheros como directorios.
            for dir in dirs: # Recorre cada uno de los archivos y directorios
                if os.path.isdir(dir): # Filtra por directorio
                    print(dir) # Los muestra por pantalla
        elif resp.lower() == "no": # Si no quieres crear, te devuelve al menú
            print("Volviendo al menú...")
        else: # Cualquier cosa que no sea SI, SÍ, si, sí, NO, no se considera no válido.
            print("El valor que has introducido no es válido.")
    except ValueError:
        print("Error.")

def api_cons():
    """Intenta conectar con la API de GitHub, si establece la conexión, muestra el código de estado y los
    primeros 200 caracteres encontrados en la recogida de información del GET de la URL. Si no tiene
    conexión la API, mostrará error de conexión, evitando que el programa se rompa."""
    try: # Intento...
        respuesta = requests.get("https://api.github.com") # Guardamos la respuesta de la URL a consultar.
        print("\nCódigo de estado:", respuesta.status_code) # Mostramos el código de estado.
        print("\nPrimeros 200 caracteres de la respuesta:\n")
        print(respuesta.text[:200]) # Mostramos primeros 200 caracteres de la respuesta al GET de URL.
    except requests.ConnectionError: # Excepción para evitar que se provoquen errores -> Si no hay conexión
        # esta excepción lo manejará, indicando que la API no está disponible, evitando que el programa se rompa.
        # Para las pruebas estuve usando requests.get("https://aaapi.github.com").
        print("Error de conexión, la API no está disponible.")

def main_menu():
    """Simple menú principal que muestra por pantalla y llama a funciones."""
    bucle = 0 # Definir bucle = 0
    while bucle == 0:
        print("\n--- Menú de Herramientas ---")
        print("1. Cálculos matemáticos")
        print("2. Explorador de directorios")
        print("3. Consulta a API (requests)")
        print("4. Salir")

        try:
            opcion = int(input("Inserta una de las opciones (valor entero) -> "))
            if opcion == 1:
                calc_mat()
            elif opcion == 2:
                os_exp()
            elif opcion == 3:
                api_cons()
            elif opcion == 4:
                print("Saliendo del menú...")
                bucle = 1 # Para salir defines bucle = 1 y se para el bucle.
            else:
                print("Opción no válida.")
        except ValueError:
            print("El valor ingresado no es entero.")

main_menu()