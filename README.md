# Hospital Api

## Descripcion
REST API que sirve endpoints para un Hospital.

## DEMO
La aplicación está disponible en docker. 
Para ello necesitas tener instalado docker y  docker-compose.
Para levantar los servicios, solo hay que estar ubicado en la ubicación del proyecto y ejecutar `docker-compose up`
Dentro de la carpeta raíz, se encuentra el backup de una collection POSTMAN. El archivo se llama `BackUp_POSTMAN_Hospital.postman_collection.json`. Con dicha collection se puede probar la API de una forma más interactiva.
El host es `localhost:5000`

## Base de datos
La base de datos usada es Postgresql. Se encuentra en el contenedor llamado postgres.
Para acceder a la base de datos, en la terminal, iniciar el contenedor postgres:
```
# Iniciar el contenedor
docker exec -it postgres bash

#Ejecutar la base de datos
su - postgres
psql

```

Por si de pronto no existe la base de datos, siga las siguientes instrucciones:

```
#Crear usuario hospital
#Dentro del contenedor
su - postgres
createuser hospital --interactive
psql
alter user hospital with password ‘hospital’;
CREATE DATABASE hospital WITH OWNER = hospital ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8' TABLESPACE = pg_default CONNECTION LIMIT = -1;

```
Terminado los pasos anteriores, pueden copiar y pegar todo el contenido del archivo `analisis_disenyo/tablas.sql` a la terminal o dentro de pgAdmin.
