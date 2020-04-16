# Scripts para ejecutar Paprika

Este repositorio contiene dos script para ejecutar los comandos de paprika. El primero llamado ```analyser.py``` para lanzar la ejecución
del análsis de una aplicación y el segundo ```analyser.py``` para ejecutar las consultas. 

## Análisis de un grupo de aplicaciones:

Para ejecutar el análisis de un grupo de aplicaciones se deben cumplir ciertos requerimientos para su correcto funcionamiento:

* Un directorio con un grupo de aplicaciones en el mismo nivel que el archivo ```analyser.py```. En el repositorio viene un grupo de seis aplicaciones.

* El repositorio de paprika de encontrarse al mismo nivel que el archivo ```analyser.py```.

El script se ejecuta utilizando el siguiente comando: 
```
python analyser.py appdir dbdir /path/to/android_platforms/
```

Las rutas para los directorios ```appdir``` y ```dbdir``` son relativas al archivo ```analyser.py```. Sin embargo, el directorio de los Android Platforms es absoluto.

## Consultas a la base de datos:

Para lanzar las consultas a la base de datos usando el modo de consultas se debe ejecutar el archivo ```queries.py```. Utilizando el comando:

```
python queries.py dbdir
```

```dbdir``` es una ruta absoluta al archivo ```queries.py```.