# Proyecto de Sistema Operativo en Docker

Este proyecto es un entorno Docker que configura un sistema operativo basado en Ubuntu con varias herramientas de desarrollo y utilidades instaladas. 

## Contenidos

1. [Descripción](#descripción)
2. [Requisitos](#requisitos)
3. [Configuración](#configuración)
4. [Ejecución](#ejecución)
5. [Comandos Útiles](#comandos-útiles)

## Descripción

El sistema operativo configurado en esta imagen Docker incluye las siguientes herramientas:

- **nano**: Editor de texto básico.
- **zip/unzip**: Herramientas para comprimir y descomprimir archivos.
- **tree**: Muestra la estructura de directorios y archivos en forma de árbol.
- **python3 y python3-pip**: Python 3 y su gestor de paquetes.
- **build-essential**: Herramientas de desarrollo esenciales, incluyendo el compilador de C.
- **python3-dev**: Cabeceras y librerías necesarias para el desarrollo en Python.
- **gdb**: Depurador de GNU.

## Requisitos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

- Docker
- Docker Compose (opcional, pero recomendado para gestionar contenedores)
- Powershell (para ejecutar el script `run.ps1` en Windows)

## Configuración

### Dockerfile

El archivo `Dockerfile` usado para crear la imagen de Docker es el siguiente:

```Dockerfile
# Usa una imagen base de Ubuntu
FROM ubuntu:20.04

# Actualiza los repositorios y instala herramientas básicas
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
```
## Ejecución
Sigue estos pasos para construir y ejecutar el contenedor:

1. Clona el repositorio o descarga los archivos en tu máquina local.
2. Abre PowerShell con permisos administrativos.
3. Navega al directorio donde se encuentran el Dockerfile y run.ps1.
4. Ejecuta el script run.ps1:
```
.\run.ps1
```
Esto construirá la imagen Docker y luego ejecutará un contenedor interactivo basado en esa imagen.

## Comandos útiles
Una vez dentro del contenedor, puedes utilizar los siguientes comandos:
- nano: Editar archivos de texto.
```
nano calculadora.py
```

- Compilar un programa en C:
```
gcc -o programa programa.c
```
- Ejecutar un script de Python:
```
python3 script.py
```
- Ver estructura de directorios:
```
tree
```
