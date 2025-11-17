# 🔹 CRUD Template — using ID (NIF) as the key

people = {}  # Main dictionary: {nif: {name, age, city, profession}}

def create_person(persona):
    # pass  # TODO: Ask for ID, name, age, city, profession and add to people
    if len(dni) == 9:
        key = persona.get("DNI")
        people[key] = persona
    else:
        print("DNI incorrecto.")

def read_people(buscar_dni):
    # pass  # TODO: Loop through people and print their info
    if buscar_dni in people:
        print(people[buscar_dni])
    else:
        print("no existe dni")

def update_person(tudni):
    """Update information of an existing person."""
    # pass  # TODO: Ask for ID, check if exists, and update fields
    key = persona.get("DNI")
    key2 = persona.get("midni")
    print(f"Has seleccionado el usuario, {key}")


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
            persona = {"DNI": dni, "Nombre": nombre, "Edad": edad, "Ciudad": ciudad, "Profesion": prof}
            create_person(persona)
        case "2":
            dnis = []
            dni = 1
            while dni != -1:
                dni = input("Introduce un DNI o -1 para parar -> ")
                dnis.append(dni)
            print("Bucle terminado")
            read_people(dnis)
        case "3":
            print(people)
            tudni = input("¿Qué usuario quieres modificar?")
            update_person(tudni)
        case "4":
            delete_person()
        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")
