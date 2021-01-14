# Hospital Api

## Descripcion
REST API que sirve endpoints para un Hospital.

## DEMO
La aplicación está disponible en docker. 
Para ello necesitas tener instalado docker y  docker-compose.
Para levantar los servicios, solo hay que estar ubicado en la ubicación del proyecto y ejecutar `docker-compose up`
Dentro de la carpeta raíz, se encuentra el backup de una collection POSTMAN. El archivo se llama `BackUp_POSTMAN_Hospital.postman_collection.json`. Con dicha collection se puede probar la API de una forma más interactiva.
El host es `localhost:5000`

Ejecutando `curl localhost:5000/api/v1/` se puede comprobar que la API service está en funcionamiento

### endpoints

+ /api/v1/
+ /api/v1/login
+ /api/v1/signin
+ /api/v1/signin/pass/<string:id>
+ /api/v1/patient/<string:id>
+ /api/v1/hospital/<string:id>
+ /api/v1/hospital/<int:id>/doctor

#### Ejemplo

+ `localhost:5000/signin/pass/21999111`
+ `localhost:5000/login`