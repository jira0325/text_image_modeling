FROM python:3.10

# Installer Git
RUN apt-get update && apt-get install -y git

# Copier d'abord les fichiers de dépendances et installer les dépendances
WORKDIR /model
COPY requirements.txt /model/
RUN pip3 install --no-cache-dir -r requirements.txt

# Ajouter les fichiers du modèle
COPY model.py /model/

# Exposer le port (si nécessaire)
EXPOSE 8000

# Définir la commande par défaut pour démarrer le modèle
CMD ["python3", "model.py"]
