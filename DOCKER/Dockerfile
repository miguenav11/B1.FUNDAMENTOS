# 1. Elegir la imagen base
# Imagen base ligera con Python
FROM python:3.11-slim
# 2. Establecer el directorio de trabajo (dentro) del contenedor
WORKDIR /app
# 3. Copiar los archivos del proyecto (el script) al contenedor
COPY . .
# 4. Definir el comando que se ejecutará al iniciar el contenedor (arranca la aplicación)
# Ejecuta Python y corre el archivo main_docker.py por defecto
CMD ["python", "main_docker.py"]