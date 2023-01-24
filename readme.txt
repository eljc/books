django-admin startproject books
cd books

python -m venv venv


pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

add rest_framework into INSTALLED_APPS

pip freeze > requirements.txt

python manage.py runserver

uvicorn bityli.main:app --reload