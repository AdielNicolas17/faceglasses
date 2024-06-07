# Use uma imagem base oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Instale dependências de sistema necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    gcc \
    g++ \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copie os arquivos de requisitos
COPY requirements.txt requirements.txt

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Exponha a porta que o Flask usará
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
