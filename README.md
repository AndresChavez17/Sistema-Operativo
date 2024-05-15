# Sistema-Operativo

Proyecto de Sistema Operativo en Docker
Este proyecto es un entorno Docker que configura un sistema operativo basado en Ubuntu con varias herramientas de desarrollo y utilidades instaladas.

Contenidos
Descripción
Requisitos
Configuración
Ejecución
Comandos Útiles
Descripción
El sistema operativo configurado en esta imagen Docker incluye las siguientes herramientas:

nano: Editor de texto básico.
htop: Monitor de sistema interactivo.
zip/unzip: Herramientas para comprimir y descomprimir archivos.
python3 y python3-pip: Python 3 y su gestor de paquetes.
build-essential: Herramientas de desarrollo esenciales, incluyendo el compilador de C.
gdb: Depurador de GNU.
x11-apps: Conjunto de aplicaciones X11, incluyendo xcalc (calculadora gráfica).
Requisitos
Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

Docker
Docker Compose (opcional, pero recomendado para gestionar contenedores)
Powershell (para ejecutar el script run.ps1 en Windows)

#Configuración
Dockerfile
El archivo Dockerfile usado para crear la imagen de Docker es el siguiente:
# Usa una imagen base de Ubuntu
FROM ubuntu:20.04

# Actualiza los repositorios y instala algunas herramientas básicas
RUN apt-get update && apt-get install -y \
    nano \
    htop \
    python3 \
    python3-pip \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Configuración por defecto del contenedor
CMD [ "bash" ]
