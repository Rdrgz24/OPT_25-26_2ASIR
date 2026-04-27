# WordPress Auto Deploy (FastAPI + Docker)

### La función de este programa, no es otra que desplegar WordPress con una base de datos de MariaDB vinculada haciendo uso de FastAPI para recoger los datos por un formulario en POST y lanzando contenedores Docker vinculados con una red interna.

### Todo el proceso de configuración e instalación están automatizados, solo se tiene que ejecutar un script .bat y enviar el formulario POST.

## Requisitos

- Sistema Operativo Windows (al menos es con el que se ha probado)
- Python con la versión 3.10 en adelante
- Docker Desktop

## Librerías utilizadas

 · FastAPI: Framework web moderno y rápido para construir APIs en Python.

 · Pydantic: Utilizado para la validación de datos de entrada en la API.

 · subprocess (estándar): Permite ejecutar comandos del sistema (Docker en este caso).

 · time (estándar): Se usa para introducir pausas durante el despliegue.

 · pwd_utils (custom): Genera contraseñas seguras automáticamente.

## Pasos para ejecutar el programa

El que de verdad nos lanza el comando main.py es:

**start.bat**

Este .bat nos instala todas las dependencias de Python requeridas (todas las que están dentro de requirements.txt) para el proyecto usando pip dentro de un entorno venv

Tras instalar y ejecutar todos los servicios, nos lanza FastAPI y se mantiene escuchando por el puerto local 8000:

**http://127.0.0.1:8000**

## Uso para desplegar WordPress

En realidad, se puede hacer de cualquier forma, creando un formulario HTML pequeño con el name e id de las variables recogidas, usando Postman o usando CURL dentro del CMD.

En este caso, yo he estado usando el siguiente comando:

**curl -X POST http://127.0.0.1:8000/deploy -H "Content-Type: application/json" -d "{\"wordpress_user\":\"admin\",\"wordpress_db\":\"wordpress\"}"**

Este comando, nos lanza un **JSON** por el formulario **POST** hacia **FastAPI** con:

**· wordpress_user: admin**

**· wordpress_db: wordpress**

Las variables pueden cambiarse sin problemas, tener en cuenta que solo cambia el usuario de WordPress y la base de datos.

## Funcionamiento general

 · Limpieza inicial:

1. Elimina contenedores, red y volumen previos si existen.

2. Creación de infraestructura:

    2.1 Crea una red Docker (wordpress_net).

    2.2 Lanza un contenedor de MariaDB.

    2.3 Lanza un contenedor de WordPress.

3. Configuración automática:

   3.1 Genera una contraseña segura.

   3.2 Configura wp-config.php usando WP-CLI.
   
4. Instalación de WordPress:

   4.1 Ejecuta la instalación base con los datos proporcionados.

   4.2 Crea el usuario administrador automáticamente.

5. Resultado: Devuelve la URL del sitio junto con las credenciales de acceso.

## Resultado

El resultado esperado es, dentro de la siguiente URL:

**http://localhost:8080**

Tener un WordPress desplegado vinculado a una base de datos de MariaDB, todo automatizado, incluso la instalación :)

## Respuesta

La respuesta configurada en el script main.py si el despliegue fue exitoso es la siguiente:

{

"status": "ok",

"url": "http://localhost:8080",

"user": "admin",

"password": "password_generada_por_pwd_utils.py"

}