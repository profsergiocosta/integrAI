# Use uma imagem leve do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas arquivos necessários
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

COPY .chainlit .

# Expõe a porta que será usada
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["chainlit", "run", "app.py", "--port", "8080", "--host=0.0.0.0"]