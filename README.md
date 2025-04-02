# README - CRUD con Python, Flask y MongoDB
## Descripción del Proyecto

Este proyecto es una aplicación CRUD (Create, Read, Update, Delete) desarrollada con:

- Python como lenguaje principal

- Flask como framework web

- MongoDB como base de datos NoSQL

La aplicación permite gestionar productos, incluyendo su nombre, precio y cantidad, con una interfaz amigable construida con HTML y Bootstrap.

## Características principales
- Formulario para agregar nuevos productos

- Visualización de todos los productos en una tabla

- Funcionalidad para editar productos existentes

- Opción para eliminar productos

- Integración completa con MongoDB (las operaciones se reflejan directamente en la base de datos)

## Requisitos del sistema
Python 3.7 o superior

MongoDB instalado y en ejecución


## Dependencias


- Flask-PyMongo

- python-dotenv


## Instalación

Clonar el repositorio:

```

bash

cd [nombre del directorio del proyecto]

git clone [https://github.com/juanpBB/CRUD.git]


```

## estructura del proyecto


```

/CRUD_MONGO
│   app.py                  # Archivo principal de la aplicación Flask
│   database.py             # Archivo para operaciones con MongoDB (modificado - indicado por "M")
│   product.py              # Archivo con definiciones de modelos/productos
│   dbb_products_app_products.json  #exportacion a de los datos de la base de datos

│
├───templates/              # Carpeta de plantillas HTML
│       index.html          # Plantilla principal del CRUD
│
└───__pycache__/            # Carpeta de caché de Python (generada automáticamente)

Copy
http://localhost4000



```

## Uso de la aplicación
- Agregar un producto:

- Completa el formulario con nombre, precio y cantidad

- Haz clic en "Enviar" para guardar el producto

## Ver productos:

- Todos los productos se muestran en la tabla debajo del formulario

- Editar un producto:

- Haz clic en el botón "Editar" de cualquier producto

- Modifica los campos en el formulario que aparecerá

- Guarda los cambios

## Eliminar un producto:

- Haz clic en el botón "Eliminar" del producto que deseas quitar

- Confirma la acción

## Configuración de MongoDB
La aplicación espera que MongoDB esté ejecutándose localmente en el puerto predeterminado (27017). Si se quiere utilizar en una base de datos propia se debe cambiar MONGO_URI con el link de acceso de tu base de datos mongo DB



## Contacto
Para preguntas o soporte, contactar al desarrollador: 
gmail:  jblandonbarbosa@gmail.com


imagenes adjuntas del proyecto CrudMongoDB
