# CONVIVE APP
Aplicación de convivencia escolar. 
En el siguiente documento se condensara todo conocimiento adquirido tanto en en la configuración de su entorno
como el historial de errores surgidos hasta ahora, con el proposito de acelerar el proceso de entendimiento del entorno necesario para esta app. 
## 1 Configuracion Entorno
### 1.1 Desarrollo
Utilizando CMD
- `git clone` el proyecto
- instalar dependencias _(consultar punto 2)_
- `pip install -r requirements.txt`
- `python manage.py makemigrations` Requiere tener creada la base de datos
- `python manage.py migrate` Requiere tener creada la base de datos
- `python manage.py runserver` Se ejecutara por defecto en 127.0.0.1:8000
### 1.2 Produccion y QA por IIS
#### 1.2.1 Preinstalaciones
- IIS
    - CGI _necesario_
- Python 3.10 con PATH configurado
#### 1.2.2 Preparar el entorno
- En `C:\` crear carpeta `virtualenvs` _(la carpeta debe tener permiso de IIS_IUSRS)_
- Dentro de `C:\virtualenvs` abrir CMD y crear entorno `python -m venv Eric` 
- Entrar desde la consola y ejecutar `Scripts\activate.bat`
- Ir a directorio del proyecto
- Instalar Handler `pip install wfastcgi` y activar `wfastcgi-enable`
-  _Seguir los pasos del punto 1.1_
#### 1.2.3 Configurar IIS
- Agregar Sitio direccionando la aplicación
- En Configuracion de FastCGI agregar aplicación
    - Ruta de Acceso Completa: ubicacion de python.exe ej: `C:\Program Files\Python310\python.exe`
    - Argumentos: ubicación de archivo wfastcgi.py ej: `C:\pyvirtualenv\Eric\Lib\site-package\wfastcgi.py`
    -Variables de Entorno: _necesario_
        - PYTHONPATH : ubicación del proyecto ej: `C:\pyvirtualenv\pise-app`
        - WSGI_HANDLER: controlador wsgi de manage.py ej: `config.wsgi.application`
        - DJANGO_SETTINGS_MODULE: archivo setting del proyecto ej: `config.settings`
- Verificar web.config del proyecto que tenga la sig linea en la etiqueta <handlers> : (Este debe ser acorde a la configuración de FastCGI)
     - `<add name="Python FastCGI" path="*" verb="*" modules="FastCgiModule" scriptProcessor="C:\Program Files\Python310\python.exe|C:\pyvirtualenv\Eric\Lib\site-packages\wfastcgi.py" resourceType="Unspecified" requireAccess="Script" />`
- Convertir en Directorio virtual la carpeta `media\` y `static\`
- Reiniciar Sitio Web
#### 1.2.4 Configurar Firewall
- Crear una regla de entrada que permita la conexion a la aplicación
## 2 Dependencias py
Para instalar las dependencias utilizar el siguiente comando por CMD `pip install [dependencia]` dentro de la carpeta contenedora del proyecto.
- Pandas
    - xlrd
    - openpyxl
- Pillow
- Django-Storages
## 3 Bitacora Errores
- El sitio responde error 400 : Consultar punto 1.2.3
- El sitio responde error 403 : Verificar los permisos, consultar punto 1.2.2
- No es posible acceder al sitio desde una conexion remota: Consultar punto 1.2.4
- Al cargar Nomina de Alumnos el sitio se actualiza sin realizar ninguna acción: Verificar dependencias instaladas, consultar punto 2
- Archivos contenidos en media o statics son inaccesibles: Verificar existencia de `web.config` en ambos directorios
- 'No module named '[depemdencia]' : Revisar dependencias faltantes en el punto 2
- 'FATAL:  database "DBName" does not exist : Es necesario verificar la BD si fue creada con el nombre que aparece en `Settings.py`
