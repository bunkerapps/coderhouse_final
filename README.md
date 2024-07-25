# SuperBlog

SuperBlog es un proyecto final del curso de Python en CoderHouse. Este proyecto es un blog desarrollado con Django, que permite a los usuarios crear, editar y eliminar publicaciones, así como interactuar con otros usuarios.


## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/bunkerapps/coderhouse_final
    cd coderhouse_final
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones:
    ```sh
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Uso

- Accede a la página principal en `http://127.0.0.1:8000/`.
- Regístrate o inicia sesión para crear, editar y eliminar publicaciones.
- Navega a las diferentes secciones del blog utilizando la barra de navegación.

## Estructura de Directorios

- `blogs/`: Contiene la lógica principal del blog, incluyendo modelos, vistas, formularios y URLs.
- `media/`: Almacena las imágenes subidas por los usuarios.
- `static/`: Contiene archivos estáticos como CSS, JavaScript e imágenes.
- `templates/`: Contiene las plantillas HTML para las diferentes vistas del blog.
- `users/`: Contiene la lógica relacionada con la gestión de usuarios, incluyendo formularios y vistas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para cualquier consulta, puedes contactarme a través de mi perfil de GitHub: [bunkerapps](https://github.com/bunkerapps).
