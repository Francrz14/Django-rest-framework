# Django-rest-framework

# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual
# En Windows:
.\env\Scripts\activate
# En MacOS y Linux:
source env/bin/activate

# Instalar Django y Django REST Framework
pip install django djangorestframework

# Crear el proyecto y la aplicación
django-admin startproject myproject
cd myproject
django-admin startapp myapp

# Guardar las dependencias en un archivo
pip freeze > requirements.txt

# Desactivar el entorno virtual cuando termines
deactivate
