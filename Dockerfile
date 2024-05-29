# imagen base de Ubuntu
FROM ubuntu:20.04

# Actualizar los repositorios e instalar editor de texto, lenguaje de programacion, 
RUN apt-get update && apt-get install -y \
    nano \
    tree \
    zip \
    unzip \
    python3 \
    python3-pip \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Configuración por defecto del contenedor
CMD [ "bash" ]