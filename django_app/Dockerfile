# Dockerfile para Django
FROM python:3.10.12-slim


WORKDIR /app

# Instala dependências do sistema necessárias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

COPY . /app/

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# Aplicar migrações e coletar arquivos estáticos
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
