#!/bin/sh

echo "Generando migraciones del proyecto Django CRM"
python manage.py migrate
python manage.py makemigrations prueba
python manage.py migrate prueba
echo "Generando Archivos estaticos............"
python manage.py collectstatic --noinput
echo "Levantando el Servidor Django"
python manage.py runserver 0.0.0.0:8000