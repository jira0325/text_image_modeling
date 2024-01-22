FROM python:3.10

# Installer Git
RUN apt-get update && apt-get install -y git

# Copier d'abord les fichiers de dépendances et installer les dépendances
WORKDIR /app
COPY requirements.txt /app/
RUN pip cache purge

RUN pip install --no-cache-dir -r requirements.txt

# Ajouter les fichiers du mpodèle
COPY main.py /app/

# Exposer le port (si nécessaire)
EXPOSE 8000

# Définir la commande par défaut pour démarrer le modè,le
CMD ["python", "main.py"]