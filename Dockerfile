# Use uma imagem base do Python
FROM python:3.12

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libev-dev \
    python3-pip

# Instalar a biblioteca cassandra-driver
RUN pip install cassandra-driver

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o script Python e arquivos CSV para o contêiner
COPY ingestao.py /app/ingestao.py
COPY data /app/data

# Comando padrão para executar o script
CMD ["python", "ingestao.py"]
