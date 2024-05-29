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
Una vez dentro del archivo calculadora.py con nano copia y pega el siguiente codigo:
```
# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def main():
    while True:
        print("Calculadora básica")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(num1, num2))
        elif opcion == "2":
            print("Resultado:", resta(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado:", division(num1, num2))
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
```
Guardalo oprimiendo CRTL + O y luego presiona la tecla Enter. 
```
CRTL + O
```
Para cerrar el archivo calculadora.py presiona CTRL + X.
```
CTRL + X
```
Concedele permisos de ejecución, escritura y lectura al archivo que recien creaste con el comando chmod:
```
chmod 777 calculadora.py
```
Ejecute el programa de calculadora.py con el siguiente comando:
```
python3 calculadora.py
```
- Crear y compilar un programa en C:
Crea un archivo .c con nano como lo hiciste anteriormente y copia y pega el siguiente codigo:
```
#include <stdio.h>

int main() {
    char operador;
    float num1, num2;

    printf("Ingrese el operador (+, -, *, /): ");
    scanf("%c", &operador);

    printf("Ingrese dos números: ");
    scanf("%f %f", &num1, &num2);

    switch (operador) {
        case '+':
            printf("Resultado: %.2f\n", num1 + num2);
            break;
        case '-':
            printf("Resultado: %.2f\n", num1 - num2);
            break;
        case '*':
            printf("Resultado: %.2f\n", num1 * num2);
            break;
        case '/':
            if (num2 != 0)
                printf("Resultado: %.2f\n", num1 / num2);
            else
                printf("Error: División por cero\n");
            break;
        default:
            printf("Operador no válido.\n");
    }

    return 0;
}
```
Guarda el archivo calculadora.c y sal del editor nano con los comandos usados anteriormente. 
```
CTRL + O
CTRL + X
```
Concedele permisos de ejecución, escritura y lectura al archivo que recien creaste con el comando chmod:
```
chmod 777 calculadora.c
```
Ahora puedes compilar el programa en c que recien creaste con esta linea de comando:
```
gcc -o calculadora cañculadora.c
```
- Ejecutar el archivo calculadora.c:
```
./calculadora.c
```
- Ver estructura de directorios:
```
tree
```
