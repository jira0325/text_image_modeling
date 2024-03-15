FROM python:3.10

# Installer Git
RUN apt-get update && apt-get install -y git

WORKDIR /streamlit
#COPY requirements.txt ./requirements.txt
RUN pip install streamlit requests
#EXPOSE 8501
COPY application_sreamlit.py /streamlit
#ENTRYPOINT [ "streamlit", "run" ]
#CMD ["application_sreamlitpy"]
# Commande par défaut pour exécuter l'application Streamlit
CMD ["python3", "-m", "streamlit", "run", "application_stramlit.py", "--server.port", "8501"]
