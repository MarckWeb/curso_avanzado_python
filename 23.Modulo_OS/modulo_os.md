# Módulo os

El módulo os en Python proporciona una forma de utilizar las funcionalidades dependientes del sistema operativo. Estas funciones son en su mayoría relacionadas con la interacción con el sistema de archivos del sistema operativo.

## Importando el módulo OS

Para utilizar el módulo os, primero debe ser importado:

```py
import os
```

## Navegación en el sistema de archivos

Python utiliza el módulo os para interactuar con el sistema de archivos. Esto incluye obtener información sobre el sistema de archivos, cambiar el directorio de trabajo actual, verificar el contenido de un directorio, etc.

Por ejemplo, para cambiar el directorio de trabajo actual, se puede utilizar **os.chdir():**

```py
os.chdir("/ruta/al/nuevo/directorio")
```

Para obtener el directorio de trabajo actual, se puede utilizar **os.getcwd():**

```py
ruta_actual = os.getcwd()
print(ruta_actual)
```

Para listar los archivos y directorios en el directorio actual, se puede utilizar _**os.listdir():**_

```py
contenido_directorio = os.listdir()
print(contenido_directorio)
```

## Creación y eliminación de directorios

El módulo os también permite crear y eliminar directorios.

Por ejemplo, para crear un nuevo directorio, se puede utilizar **os.mkdir():**

```py
os.mkdir("nuevo_directorio")
```

Para eliminar un directorio, se puede utilizar **os.rmdir():**

```py
os.rmdir("directorio_a_eliminar")
```

Para crear varios directorios de una sola vez, se puede utilizar **os.makedirs()**, que puede crear todos los directorios intermedios si no existen:

```py
os.makedirs("dir1/dir2")
```

## Manipulación de archivos

Además de trabajar con directorios, el módulo os también proporciona varias funciones para trabajar con archivos.

Por ejemplo, para renombrar un archivo, se puede utilizar **os.rename():**

```py
os.rename("nombre_original.txt", "nombre_nuevo.txt")
```

Para eliminar un archivo, se puede utilizar **os.remove():**

```py
os.remove("archivo_a_eliminar.txt")
```

## Variables de entorno

Las variables de entorno son un tipo de variable que el sistema operativo utiliza para almacenar información sobre el sistema y ciertos programas. El módulo os permite acceder a estas variables mediante **os.environ:**

```py
print(os.environ)
```

Este código imprimirá todas las variables de entorno del sistema. Para acceder a una variable de entorno específica, se puede hacer referencia a ella como si fuera un diccionario:

```py
ruta_python = os.environ.get('PYTHONPATH')
print(ruta_python)
```

El módulo os en Python es una herramienta poderosa que permite a los programas Python interactuar de manera más estrecha con el sistema operativo subyacente. Esto incluye tareas como navegar y manipular el sistema de archivos, acceder a las variables de entorno, y mucho más. Aunque estas tareas a menudo son más específicas del sistema que otras tareas de programación de Python, el módulo os proporciona una interfaz de alto nivel que es relativamente fácil de usar.
