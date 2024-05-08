## Introccion e instalacion de Django

Para utilizar Django, primero necesitamos instalar el programa desde la página oficial de Django: https://www.djangoproject.com.

1. Navega a la pestaña de descargas.
2. Selecciona la opción de descarga adecuada para tu sistema operativo.

La instalación se realiza mediante el uso de un entorno virtual. Para ello, sigue estos pasos:

1. Crea un directorio
2. Abre tu terminal.
3. Sitúate en el directorio donde deseas crear tu proyecto Django.
4. Ejecuta el siguiente comando para crear un entorno virtual:

```bash
python3 -m venv <nombre_virtual>
```

Por ejemplo:

```bash
python3 -m venv env_django
```

Este comando creará un directorio llamado env_django que contendrá el entorno virtual.

5. Ahora hay que activar el entorno ejecutando el siguiente comando:

```bash
# para mac
source env_django/bin/activate
```

**Nota:** Asegúrate de estar en la misma ubicación donde creaste tu entorno virtual antes de ejecutar este comando.

```bash
# para windows
source env_django/scripts/activate
```

la terminal cambiara el promt a (env_django), indica que se esta trabajando dentro de un entorno virtual.
