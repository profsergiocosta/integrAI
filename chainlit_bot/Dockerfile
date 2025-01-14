# Dockerfile para Chainlit
FROM python:3.10-slim

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["chainlit", "run", "bot.py"]
