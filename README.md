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


## imagenes adjuntas del proyecto CrudMongoDB

- Diagrama de casos de uso

![image](https://github.com/user-attachments/assets/c6a580b9-7baa-419d-887e-77bf1a05c8af)

- como se ve en mongodb


 ![image](https://github.com/user-attachments/assets/02e7c1e0-e26c-4cb5-9642-f33f06ddca8e)

- estructura de la tabla mysql (hecha en heidiSQL)


![image](https://github.com/user-attachments/assets/ffbf7231-4f82-45ba-8f3b-3ce3fef96471)

- como se ve en XAMP


![image](https://github.com/user-attachments/assets/1c28184f-5499-46f7-9cef-c03b70179ee2)
