# Scripts para ejecutar Paprika

Este repositorio contiene dos script para ejecutar los comandos de paprika. El primero llamado ```analyser.py``` para lanzar la ejecución
del análsis de una aplicación y el segundo ```analyser.py``` para ejecutar las consultas. 

## Análisis de un grupo de aplicaciones:

Para ejecutar el análisis de un grupo de aplicaciones se deben cumplir ciertos requerimientos para su correcto funcionamiento:

* Un directorio con un grupo de aplicaciones. En el repositorio viene un grupo de seis aplicaciones.

* El repositorio de paprika de encontrarse al mismo nivel que el archivo ```analyser.py```

El proyecto principal se encuentra en la carpeta monitor-de-emprendimientos-para-openbeauchef, que contiene las configuraciones globales del proyecto en ```settings.py```, las urls por defecto que mappeara django desde los request estarán en el archivo ```urls.py```.

Ademas se generan app's (emprendimientos, ficha, personas, etc.) en sus carpetas respectivas. Cada una de estas tendrá consigo:
* templates : Carpeta que contiene los archivos html correspondientes a las vistas de la app.
* urls.py : Archivo que contiene las rutas y conexiones con las funciones respuestas.
* views.py : Archivo que contiene la lógica de respuestas a las peticiones.
* models.py : Archivo que contiene las clases que representan los objetos que el ORM de django mappeara y guardara en la base de datos.

Los estáticos del projecto estarán en la carpeta ```static```

## Requisitos del proyecto
Para la correcta ejecución de este proyecto se requiere python 3 y pip. 

## Instalación del proyecto

Para instalar y hacer correr esta plataforma se recomienda el uso de un ambiente virtual, herramientas como [virtualenv](https://virtualenv.pypa.io/en/stable/) o su [wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) son altamente recomendadas, primero se deben instalar las dependencias del proyecto señaladas en el archivo ```requirements.txt```, para esto se puede utilizar el comando 
``` pip install -r path/to/requirements.txt ```
 ya con esto solo debemos crear la base de datos, lo cual se puede hacer mediante los comandos
 ``` 
 django /path/to/manage.py makemigrations
 django /path/to/manage.py migrate
 ```