# BackEnd EV1
cd agenda_contactos
python -m venv venv
mandar el activate a la terminal
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

**python manage.py runserver**(ya no se usa)

python manage.py createsuperuser

python manage.py collectstatic

si no funciona al iniciar escribir: cd .. y hacer migraciones
