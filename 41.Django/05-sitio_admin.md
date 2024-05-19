# Introducción al sitio de administración de Django

django tiene su propio sistema de administracionn para mejorar y ahcer rapidamente aplicaciones webs

## Creación de usuarios

Cuando cree proyectos, la interfaz de administración se creará automáticamente, pero no configurará ningún acceso de usuario. Para iniciar sesión en el sitio de administración de Django, ahora necesitamos crear el primer usuario, que es un superusuario.

## Creación de un superusuario

asegurarse de que esta activo el entorno virtual

```bash
source env/Scripts/activate
```

Ejecute el comando siguiente para crear un superusuario:

```bash
python manage.py createsuperuser
```

el en navegador ir a http://127.0.0.1:8000/admin/ y introducir las credenciales para accerder al administrador de django

## Creación de un usuario de personal

1. click en users

2. En la esquina superior derecha, seleccione AGREGAR USUARIO.

3. Escriba un nombre de usuario para staffuser.

4. Escriba una contraseña que cumpla los requisitos de complejidad y confírmela.

5. Seleccione SAVE (GUARDAR).

6. En la pantalla siguiente, seleccione Staff status (Estado de personal) para que el nuevo usuario sea de personal

## Administración de datos

Como ya se indicó antes, el sitio de administración no proporciona acceso a los datos de forma predeterminada. Afortunadamente, solo necesita un par de líneas de código para registrar los modelos que quiera que se puedan editar a través de la herramienta.

## Registro de modelos

Abra mi_aplicacion/admin.py.

Debajo del comentario # Register your models here., agregue el código siguiente para registrar los modelos.

```py
from .models import Categoria, Producto

admin.site.register(Categoria)
admin.site.register(Producto)
```

Volver al explorador, actualizar y verificar los cambios que salne debajo.

## Acceso a los datos

Ahora que hemos registrado los modelos, podemos administrar los datos. Si ya había datos en la base de datos, podemos modificarlos, en caso de que sea necesario.

- seleccionar agregar productos
- seleccionar signo verde +
- escribir datos de la caregoria
- seleccionar guardar
- escribir datos del producto
- seleccionar guardar y se vera el producto en el listado
- selecciomnar al productos y se dirigira a la pagian detalles donde se pùede modificar los datos

## Establecimiento de los permisos de usuario

1. Vuelva al sitio de administración en el explorador.

2. Seleccione Usuarios.

3. Seleccione staffuser para actualizar nuestro usuario de personal.

4. Asegúrese de que está seleccionado Staff status (Estado de personal).

5. Desplácese hacia abajo hasta Permisos de usuario.

6. Seleccione los permisos siguientes:

7. Vuelva al sitio de administración en el explorador.

mi_aplicacion | producto | Can add producto
mi_aplicacion | producto | Can change producto
mi_aplicacion | producto | Can view producto

## Inicio de sesión como usuario de personal

Veamos ahora la diferencia entre un superusuario y un usuario de personal. Para ello, iniciaremos sesión como usuario de personal.

1. Seleccione CERRAR SESIÓN en la esquina superior derecha.

2. Seleccione Iniciar sesión de nuevo.

3. Inicie sesión como staffuser con la contraseña que creó anteriormente.

el usuario debera tener acceso solo a productos, sinos olvidamos la contraseña se puede volver s ingresar con super usuario y hacer los cambios del usuario

## Resumen

Hemos configurado un usuario de personal con permisos limitados en el sitio de administración. Puede usar esta función para controlar el acceso a los datos confidenciales de la aplicación.
