бронирование комнат в отелях

pip install psycopg2-binary
pip freeze > requirements.txt
docker-compose build web
docker-compose up web
docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py createsuperuser
docker-compose build celery-beat
docker-compose build celery
docker-compose up celery-beat
docker-compose up celery



