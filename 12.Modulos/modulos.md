# Importar modulos y paquete

En Python, un módulo es un archivo que contiene definiciones y declaraciones de Python. El nombre del archivo es el nombre del módulo con el sufijo .py añadido. Por otro lado, un paquete es una forma de organizar módulos relacionados de Python en un directorio.

## Importar Módulos

En Python, para utilizar un módulo en un programa, primero debe ser importado. Puede importarse un módulo utilizando la declaración import.

Por ejemplo, el módulo math proporciona funciones matemáticas. Para importar este módulo, se haría lo siguiente:

```py
import math
```

Una vez que el módulo está importado, pueden utilizarse sus funciones. Por ejemplo, podría usarse la función sqrt del módulo math para calcular la raíz cuadrada de un número.

```py
import math

print(math.sqrt(16)) # 4
```

Además de importar un módulo completo, también es posible importar una función específica de un módulo. Por ejemplo, si solo se quiere usar la función sqrt del módulo math, puedes hacerse de la siguiente manera:

```py
from math import sqrt

print(sqrt(16)) # 4
```

## Importar Paquetes

Un paquete es básicamente un directorio con archivos Python y un archivo especial llamado **init**.py. Este archivo puede estar vacío, pero debe estar presente en el directorio.

Para importar un módulo desde un paquete, debe usarse el nombre del paquete seguido de un punto y luego el nombre del módulo. Por ejemplo, si se tuviera un paquete llamado my_package y hay un módulo en este paquete llamado my_module, se podría importar de la siguiente manera:

```py
import my_package.my_module
```

También es posible usar la declaración from con paquetes. Por ejemplo, para importar solo la función my_function del módulo my_module en el paquete my_package:

```py
from my_package.my_module import my_function
```

## Alias y la declaración as

Al importar un módulo o una función, es posible darle un alias. Esto es útil si el nombre del módulo o la función es largo o si se quiere evitar conflictos de nombres.

Por ejemplo, el módulo math podría ser importado con el alias m:

```py
import math as m

print(m.sqrt(16))
```

Se puede hacer lo mismo con los paquetes y las funciones:

```py
from my_package.my_module import my_function as mf

mf()
```

En este ejemplo, mf() llamaría a la función my_function del módulo my_module en el paquete my_package.

En resumen, los módulos y paquetes en Python permiten una organización de código efectiva y reutilizable. Mediante el uso de import, se puede acceder a cualquier módulo o paquete y utilizar su funcionalidad en el código.
