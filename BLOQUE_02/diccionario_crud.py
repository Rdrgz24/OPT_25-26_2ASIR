# 🔹 CRUD Template — using ID (NIF) as the key

people = {}  # Main dictionary: {nif: {name, age, city, profession}}

def create_person(persona):
    # pass  # TODO: Ask for ID, name, age, city, profession and add to people
    if len(dni) == 9:
        key = persona.get("dni")
        people[key] = persona
    else:
        print("DNI incorrecto.")

def read_people(dnis):
    # pass  # TODO: Loop through people and print their info
    for dni in dnis:
        if dni in people:
            print(people[dni])
        else:
            print("No se encuentra")

def update_person(tudni):
    """Update information of an existing person."""
    # pass  # TODO: Ask for ID, check if exists, and update fields
    if tudni in people:
        key = persona.get("dni")
        print(f"Datos actuales -> {people[tudni]}")
        opcion = input("¿Qué dato quieres editar? Nombre, edad, ciudad o profesion.")
        if opcion.lower() in ["nombre", "edad", "ciudad", "profesion"]:
            valor = input(f"Introduce el nuevo valor para {opcion}")
            people[tudni][opcion] = valor
            print("Dato actualizado correctamente.")
        else:
            print("Opción no válida.")
    else:
        print(f"DNI no encontrado.")

def delete_person():
    # pass  # TODO: Ask for ID and remove from the dictionary if exists
    persona = {"DNI": "29070819L", "Nombre": "Ana", "Edad": 20, "Ciudad": "Huelva", "Profesion": "Carpintero"}
    key = persona.get("DNI")
    people[key] = persona
    if key in people:
        del people[key]
        print(people)
# 🔸 Main menu
option = ""

while option != "5":
    print("\n=== PEOPLE CRUD MENU ===")
    print("1. Create person")
    print("2. Read people")
    print("3. Update person")
    print("4. Delete person")
    print("5. Exit")

    option = input("Choose an option: ")

    match option:
        case "1":
            dni = input("Introduce el DNI -> ")
            nombre = input("Introduce tu nombre -> ")
            edad = input("Introduce tu edad -> ")
            ciudad = input("Introduce tu ciudad -> ")
            prof = input("Introduce tu profesion -> ")
            persona = {"dni": dni, "nombre": nombre, "edad": edad, "ciudad": ciudad, "profesion": prof}
            create_person(persona)
        case "2":
            buscar = 0
            dnis = []
            while buscar != -1:
                dni = input("Introduce un DNI o -1 para parar -> ")
                dnis.append(dni)
            print("Bucle terminado")
            read_people(dnis)
        case "3":
            tudni = input("¿Qué usuario quieres modificar?")
            update_person(tudni)
        case "4":
            delete_person()
        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")