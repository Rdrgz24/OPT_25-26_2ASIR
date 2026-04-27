import secrets
import string

# Definidas letras, dígitos y caracteres especiales
l = string.ascii_letters
d = string.digits
# Aquí se puede usar la lista de secrets que tiene caracteres especiales, el problema viene cuando
# Wordpress usa las contraseñas y encuentra el carácter ' o ", ahí peta por el formato del dato
sc = "!@#%^*-_=+"

mypwd = l + d + sc # Literalmente una variable que abarca las 3 cosas

# Definimos función para generar contraseña de 20 dígitos
def pwd20():
    """
    Esta función genera una contraseña de 20 caracteres combinando:
    letras, sin mínimo
    números, con un mínimo de 3
    caracteres, con un mínimo de 1
    Realiza un bucle que será cerrado en cuanto cumpla la condición y otro bucle, realizará las
    comprobaciones para que cumpla los requisitos de complejidad
    """
    length = 20 # Indicar longitud
    n = 0 # Variable para salir de bucle cuando cumpla la condición, así envitamos usar break

    # Mientras n sea 0...
    while n == 0:
        pwd = '' # Arimos variable vacía
        for i in range(length): # i dentro de un rango de 20
            # Seleccionar un carácter aleatorio de la variable mypwd (así evita usar random)
            # y el resultado es totalmente aleatorio e impredecible, ya que usa una criptografía
            # segura, choice es interno de secrets, y es mejor que random al buscar algo aleatorio
            pwd += secrets.choice(mypwd)
        if any(char in sc for char in pwd): # Condición para que mínimo contenga un carácter
            if sum(char in d for char in pwd) >= 3: # Condición para que mínimo tenga 3 números
                n = 1 # Cerramos bucle
                return pwd # Retornamos contraseña