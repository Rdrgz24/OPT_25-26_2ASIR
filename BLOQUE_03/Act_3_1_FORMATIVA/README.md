# WordPress Auto Deploy (FastAPI + Docker)

### La función de este programa, no es otra que desplegar WordPress con una base de datos de MariaDB vinculada haciendo uso de FastAPI para recoger los datos por un formulario en POST y lanzando contenedores Docker vinculados con una red interna.

### Todo el proceso de configuración e instalación están automatizados, solo se tiene que ejecutar un script .bat y enviar el formulario POST.

## Requisitos

- Sistema Operativo Windows (al menos es con el que se ha probado)
- Python con la versión 3.10 en adelante
- Docker Desktop

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