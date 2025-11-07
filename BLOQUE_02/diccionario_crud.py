# 🔹 CRUD Template — using ID (NIF) as the key

people = {}  # Main dictionary: {nif: {name, age, city, profession}}

def create_person(persona):
    # pass  # TODO: Ask for ID, name, age, city, profession and add to people
    if len(dni) == 9:
        key = persona.get("DNI")
        people[key] = persona
    else:
        print("DNI incorrecto.")

def read_people():
    # pass  # TODO: Loop through people and print their info
    print(people)

def update_person():
    """Update information of an existing person."""
    # pass  # TODO: Ask for ID, check if exists, and update fields
    persona = {"DNI": "29070819L", "Nombre": "Ana", "Edad": 20, "Ciudad": "Huelva", "Profesion": "Carpintero"}
    key = persona.get("DNI")
    people[key] = persona
    print(people)

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
            read_people()
        case "3":
            update_person()
        case "4":
            delete_person()
        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")
