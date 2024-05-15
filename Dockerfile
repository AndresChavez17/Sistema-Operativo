# Usa una imagen base de Ubuntu
FROM ubuntu:20.04

# Actualiza los repositorios y instala algunas herramientas básicas
RUN apt-get update && apt-get install -y \
    nano \
    python3 \
    python3-pip \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Configuración por defecto del contenedor
CMD [ "bash" ]
