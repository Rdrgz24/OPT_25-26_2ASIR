from fastapi import FastAPI  # type:ignore
from pydantic import BaseModel  # type:ignore
import subprocess
import time
from pwd_utils import pwd20

app = FastAPI() # Llamamos a FastAPI y guardamos esta llamada dentro de la variable app

# Con class guardamos una plantilla / plano / molde con el que trabajar
class Datos(BaseModel): # En este caso indicamos que usará BaseModel como validador
    # todo esto, dentro de Datos, que aloja las siguientes variables:
    wordpress_user: str # Indicamos que el dado que se espera es string
    wordpress_db: str # igual


@app.post("/deploy") # Llamamos a FastAPI para que recoja formulario tipo POST desde /deploy
def deploy(data: Datos): # Definimos función llamada "deploy" y usa lo recogido desde "Datos"

    try: # Modelo de excepción, intentamos con try literalmente

        # Generar contraseña automáticamente
        pwd_generada = pwd20()

        print("\n1. Limpieza de contenedores y red ;)") # Indicamos el paso a realizar

        # Hacemos una limpieza desde shell (CMD) de los contenedores creados
        # (si hubiese previamente), redes y volumenes, ya sabemos lo que se crea,
        # por lo que, sabemos lo que se debe borrar
        subprocess.run("docker rm -f wordpress mariadb", shell=True, stderr=subprocess.DEVNULL)
        subprocess.run("docker network rm wordpress_net", shell=True, stderr=subprocess.DEVNULL)
        subprocess.run("docker volume rm wp_data", shell=True, stderr=subprocess.DEVNULL)
        # Si los contenedores no existen, no hay problema :) No se muestra por pantalla la limpieza y listo.

        print("\n2. Montamos infra :)")

        # Creamos red de docker para que base de datos y wordpress se comuniquens
        subprocess.run("docker network create wordpress_net", shell=True)

        # Luego, se crea el contenedor de docker con mariadb
        subprocess.run(
            # Desplegamos contenedor de mariadb con red asociada
            f"docker run -d --name mariadb --network wordpress_net "
            # Pasamos instrucciones para crear una base de datos con el nombre recogido
            f"-e MYSQL_ROOT_PASSWORD=rootpass "
            # Pasamos instrucciones para crear un usuario con su contraseña en base a datos recogidos
            f"-e MYSQL_DATABASE={data.wordpress_db} "
            f"-e MYSQL_USER={data.wordpress_user} "
            f"-e MYSQL_PASSWORD={pwd_generada} "
            # Indicamos finalmente la versión a descargar.
            f"mariadb:latest",
            shell=True
        )

        # Tras desplegar la base de datos, vamos con wordpress
        subprocess.run(
            # Desplegamos contenedor wordpress con red asociada y
            # puerto 8080 desde host, puerto 80 internamente
            f"docker run -d --name wordpress --network wordpress_net -p 8080:80 "
            # Indicamos el volumen (físico en nuestro equipo) que usará el contenedor 
            # y la ubicación dentro del container (var/www/html)
            f"-v wp_data:/var/www/html "
            # Lo siguiente es indicar el host
            f"-e WORDPRESS_DB_HOST=mariadb "
            # Lo siguiente es indicar el host, usuario, contraseña y nombre de base de datos
            f"-e WORDPRESS_DB_USER={data.wordpress_user} "
            f"-e WORDPRESS_DB_PASSWORD={pwd_generada} "
            f"-e WORDPRESS_DB_NAME={data.wordpress_db} "
            # Indicamos finalmente la versión a descargar.
            f"wordpress:latest",
            shell=True
        )

        print("\nEsperamos a que inicie wordpress y mariadb, paciencia porfa :)")
        time.sleep(15) # Tiempo para que MariaDB arranque y WP copie archivos
        # Este tiempo dependerá en realidad de los recursos de cada equipo donde se ejecute el script

        # Aquí veremos algo bastante chulo, ejecutamos un contenedor temporal como root, que conecta el contenedor
        # a la red donde se encuentra mariadb, monta el volumen de wordpress y carga wp-cli
        # la terminal de wordpress con el que se hará la instalación automatizada
        cli_base = "docker run --rm --user 0:0 --network wordpress_net -v wp_data:/var/www/html wordpress:cli"

        print("\n3. Configuramos wp-config.php para instalación automatizada :O")

        subprocess.run(
            # Nos permite crear wpconfig dentro de la cli
            f"{cli_base} wp config create "
            # Definimos base de datos
            f"--dbname={data.wordpress_db} "
            # Con su nombre de usuario
            f"--dbuser={data.wordpress_user} "
            # Contraseña generada por el script wena wena
            f"--dbpass={pwd_generada} "
            # Indicamos el host, nombre del container
            f"--dbhost=mariadb "
            # Forzamos posibilidad de uso de root
            f"--allow-root --force",
            shell=True,
            capture_output=True
        )

        print("\n4. Instalamos WordPress")

        inst = subprocess.run( # Lo guardamos en variable para ver el estado :)
            # Volvemos a llamar al cli, pero esta vez para la instalación de wp
            f'{cli_base} wp core install ' # Pasamos a la acción
            # Indicamos URL de acceso, importante
            f'--url="http://localhost:8080" '
            # Indicamos título de la web, visible dentro de este
            f'--title="Mi Proyecto Python" '
            # Indicamos usuario (parámetro pasado por curl o postman)
            f'--admin_user="{data.wordpress_user}" '
            # Indicamos pwd generada por el script
            f'--admin_password="{pwd_generada}" '
            # Email, el que sea, esto no me interfiere en nada
            f'--admin_email="mailejemplo@mail.com" '
            # Saltamos email de root, solo de email
            f'--skip-email --allow-root',
            shell=True,
            capture_output=True,
            text=True
        )

        # En este acso, el STDOUT contiene en este caso lo que imprime en la salida tras ejecutar
        # el comando de instalación, de ahí el porque del guardarle en una variable
        print("\n5. Estado de la instalación:")
        print("\nSTDOUT:", inst.stdout)

        # Comprobación muy básica, wordpress tras instalarse dice "WordPress installed successfully"
        # por lo que, si Success está dentro de la salida, el deploy fue correcto
        if "Success" in inst.stdout:
            # Si cumple la condición, muestra por pantalla despliegue
            print("|······DESPLIEGUE COMPLETADO······|")
            # Y además, facilita el estado, URL, usuario y la contraseña de acceso
            return {
                "status": "ok",
                "url": "http://localhost:8080",
                "user": data.wordpress_user,
                "password": pwd_generada
            }
        else:
            # De lo contrario, muestra que ha habido un error
            print("|······ERROR EN EL DESPLIEGUE······|")
            # Además, mostramos el mensaje de error.
            return {
                "status": "error",
                "detalle": inst.stderr
            }

    # Para finalizar, completamos el except con la excepción, o por así decirlo la razón del fallo,
    # guardamos esta razón dentro de "e"
    except Exception as e:
        # Además, mostramos el mensaje de la excepción
        return {
            "status": "error",
            "mensaje": str(e)
        }