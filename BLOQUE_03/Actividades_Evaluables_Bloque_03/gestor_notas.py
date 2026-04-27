"""
Este programa permite trabajar con los valores de un archivo, permitiendo visualizar, modificar y eliminar
los valores. Todo está controlado por excepciones para hacer el programa lo más estricto posible.
Se trabaja bajo el archivo "notas.txt".
"""

archivo = "notas.txt"
encoding = "utf-8"

def check_file():
    """Comprueba que el archivo existe, si existe, indica si tiene notas o no y las muestra.
    Si o existe, el archivo se crea vacío y se indica en el programa."""
    try: # Intento...
        modo = "r"
        with open(archivo, modo, encoding=encoding) as f:
            notas = f.readlines()
            if notas: # Si existen notas... recorre las notas y la muestra por pantalla
                print(f"Archivo {archivo} encontrado con notas:\n")
                for n, nota in enumerate(notas, start=1):
                    print(f"{n}.{nota.strip()}") # Uso de strip para quitar los saltos de líneas en la vista
            else: # De lo contrario, se indica que el archivo existe, pero no tiene notas
                print(f"Archivo {archivo} encontrado. Se encuentra vacío.\n")
    except FileNotFoundError: # Excepcion - No se encuentra el archivo
        print(f"El documento {archivo} no existía. Se ha creado vacío.\n") # Si no existía, se crea vacío con el modo w.
        modo = "w"
        with open(archivo, modo, encoding=encoding) as f:
            f.write("")
    except PermissionError: # Excepcion - No se dispone de permisos suficientes
        print("Error de permisos.\n")


def view_note():
    """Comprueba que hay notas dentro del archivo, si las hay, las muestra, de lo contrario, indica que no hay.
    Como excepciones añadí varias, si no encuentra el archivo (no común porque al principio del programa
    ya se llama a check_file que debe crearlo, pero por evitar problemas...) o de permisos."""
    try:
        modo = "r"
        with open(archivo, modo, encoding=encoding) as f:
            notas = f.readlines()
            if notas: # Si existen notas, las recorreo y muestra por pantalla.
                for n, nota in enumerate(notas, start=1):
                    print(f"{n}.{nota.strip()}")
            else:
                print("No hay notas dentro del archivo.\n") # De lo contrario, indica que no hay notas en el archivo
    except FileNotFoundError:
        print("El archivo no existe.\n")
        # Diría que va a ser poco necesario porque al inicio del programa ya se llama a check_file(), pero por si
        # se borrase el archivo durante la ejecución del programa, lo vuelve a crear para evitar que rompa.
        check_file() # Llamar a la función check_file() para que lo cree, en caso de no estarlo.
    except PermissionError:
        print("Error de permisos.\n")

def add_note():
    """Permite añadir notas al archivo una vez ya creado. Si introduces un valor vacío te indica que no puedes
    insertar una nota vacía, lo hagas de la manera que lo hagas. Nuevamente, llamo a check_file() por si no existiera."""
    try:
        modo = "a"
        nota = input("Introduce la nota a insertar -> ")
        if not nota.strip(): # Excepción para que no se introduzca vacío, con .strip evitamos tanto "" como "    ".
            print("No puedes introducir notas vacías.")
        else:
            with open(archivo, modo, encoding=encoding) as f: # De lo contrario, insertamos la nota sin problemas.
                f.write(f"{nota}\n")
                print("Nota insertada correctamente.")
    except FileNotFoundError:
        print("El archivo no existe.\n")
        check_file() # Llamar a la función check_file() para que lo cree, en caso de no estarlo.
    except PermissionError:
        print("Error de permisos.\n")

def del_note():
    """Primero, muestra las notas para facilitar el trabajo de borrado. Tras mostrarlas, te permite eliminar
    una de ellas, siempre controlando que el número sea mayor que 1 (ya que empieza en 1) y menor que el
    número de notas que existe en la lista. Luego se borra el elemento con notas.pop y se vuelve a reescribir
    los valores dentro del archivo."""
    try:
        modo = "r"
        print("Notas actuales:")
        view_note()
        with open(archivo, modo, encoding=encoding) as f:
            notas = f.readlines()
            if notas: # Busca notas para posibilitar la eliminación o no..
                num = int(input("Introduce el número a eliminar -> "))
                if num < 1 or num > len(notas):
                    print("Has introducido un valor fuera de rango.")
                else:
                    # Se le resta 1 porque la posición de la lista empieza en 0. Si queremos borrar la lista 3 = en posición de índice = número 2.
                    notas.pop(num - 1) # Notas.pop para borrar un elemento de la lista.
                    modo = "w"
                    # Dentro del programa, insertamos los valores de la lista tras ser borrada para actualizar el archivo.
                    with open(archivo, modo, encoding=encoding) as f:
                        for nota in notas: # Línea a comentar
                            f.write(nota)
                    print("Nota eliminada correctamente.")
            else:
                print("No hay notas, no puedes eliminar.") # Si no encuentra notas, no hay nada que eliminar.
    except FileNotFoundError:
        print("El archivo no existe.\n")
        check_file() # Llamar a la función check_file() para que lo cree, en caso de no estarlo.
    except PermissionError:
        print("Error de permisos.\n")

def main_menu():
    """Menú principal, puro print y llamada a funciones, nada del otro mundo."""
    bucle = 0 # Definimos bucle = 0 para cumplir con esa condición hasta que lo paremos dentro del bucle.
    while bucle == 0:
        print("|-------------MENU-------------|")
        print("| 1. Ver notas                 |")
        print("| 2. Añadir nota               |")
        print("| 3. Eliminar nota             |")
        print("| 4. Salir                     |")
        print("|------------------------------|")

        opcion = input("Introduce la opción a elegir -> ")

        if opcion == "1":
            view_note()
        elif opcion == "2":
            add_note()
        elif opcion == "3":
            del_note()
        elif opcion == "4":
            print("Saliendo...")
            bucle = 1 # Bucle pasa a ser 1, no cumple condición bucle = 0, lo rompe.
        else:
            print("Opción no válida.\n")

check_file() # Llamar para comprobar si existe el archivo.
main_menu() # Llamar menú para posibilitar opciones al usuario.