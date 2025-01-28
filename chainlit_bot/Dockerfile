# Dockerfile para Chainlit
FROM python:3.10-slim

WORKDIR /app
COPY . /app/
COPY .chainlit /app/.chainlit

RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install -r requirements.txt

# Define a porta desejada (por exemplo, 8500)
CMD ["chainlit", "run", "app.py", "--port", "8080", "--host=0.0.0.0"]
