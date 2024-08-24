# Tercer Pre-entrega - Curso Python
### Comisión: 57825
### Profesor: Alejandro Sosa
### Tutor: Federico Poliseno
### Alumna: Soledad Paola Rocha
## Proyecto:
Aplicación Web para Estudio de Comercio Exterior

## Versión
1.0

## Descripción del Proyecto
Aplicación Web destinada a usuarios del estudio de comercio exterior.

Hasta el momento, he desarrollado los siguientes requerimientos del usuario:
- Alta de Exportadores
- Alta de Importadores
- Alta de Mercaderías 
- Alta de Operaciones
- Busqueda de Exportadores por nombre

## Módulo de Alta de Exportadores
#### Permite registrar los datos de exportadores como nombre, domicilio, email y cuit a través de un formulario, donde se introducen estos datos para su registro. 
### Son dos formularios para agregar Exportadores.
#### Un formulario por HTML con URL: http://127.0.0.1:8000/App/expo-form/
### El otro es por Django con URL: http://127.0.0.1:8000/App/expo-form-1/

## Módulo de Alta de Importadores
#### Permite registrar los datos de importadores como nombre, domicilio, email y cuit a través de un formulario, donde se introducen estos datos para su registro.
#### Un formulario por Django para agregar Importadores.
#### URL: http://127.0.0.1:8000/App/impo-form-2/

## Módulo de Alta de Mercadería
#### Permite registrar los datos de la mercadería a importar o exportar. Ellos son el nombre de la mercadería y el tipo de unidad de venta. Se realiza su registro a través de un formulario, donde se introducen estos datos para su registro.
#### Un formulario por Django para agregar mercaderías.
#### URL: http://127.0.0.1:8000/App/merc-form-3

## Módulo de Alta de Operaciones
#### Permite registrar las operaciones realizadas, a través de un formulario, donde se ingresan datos de una operación como fecha de operación, fecha de cumplimiento, número de permiso y cantidad. 
#### Un formulario por Django para ingresar operaciones.
#### URL:  http://127.0.0.1:8000/App/oper-form-4

## Módulo de Búsqueda de datos de los Exportadores a partir del nombre
#### Permite buscar los datos de un exportador determinado, a través del ingreso de su nombre, recuperando e imprimiendo en pantalla todos los datos del exportador como Nombre, Domicilio, email y Cuit.
#### URL: http://127.0.0.1:8000/App/busquedaExportador

## Acceso a la Base de Datos
#### Usuario: solep 
#### Contraseña: devsolpao24

## Tecnologías

##### Front-End
- HTML 5
- Bootstrap 5.2

##### Back-End
- Python 3.11.9
- Django 4.2
- SQLite 3.31.0

