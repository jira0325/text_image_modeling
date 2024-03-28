
########## MYSQL ############

FROM mysql:latest

# Configuration MySQL (exemple)
ENV MYSQL_ROOT_PASSWORD=user123
ENV MYSQL_DATABASE=img_txt_project
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=user123

# Copie de fichiers SQL pour initialiser la base de données (si nécessaire)
COPY script1.sql /docker-entrypoint-initdb.d/

# Debug pour lister les fichiers dans le répertoire du Dockerfile
RUN ls -l /docker-entrypoint-initdb.d/
