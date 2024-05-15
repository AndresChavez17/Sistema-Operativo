# Construye la imagen Docker
docker build -t so_nuevo_image .

# Corre el contenedor
docker run -it --rm `
    --name so_nuevo_container `
    so_nuevo_image
