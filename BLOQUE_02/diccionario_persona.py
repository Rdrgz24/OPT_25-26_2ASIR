"""
1. Crea un diccionario persona con las claves: nombre, edad, ciudad.
2. Muestra el valor de cada clave.
3. Añade una nueva clave profesion con su valor.
4. Elimina la clave ciudad.
5. Recorre el diccionario mostrando clave y valor en cada línea.
"""

persona = {"nombre": "Rafael", "edad": 20, "ciudad": "Huelva"}
# 2. Muestra el valor de cada clave.
print(persona.values())
# 3. Añade una nueva clave profesion con su valor.
prof = {"profesion": "No especificada"}
# 4. Elimina la clave ciudad.
del persona["ciudad"]
# 5. Recorre el diccionario mostrando clave y valor en cada línea.
persona.update(prof)
print(persona)