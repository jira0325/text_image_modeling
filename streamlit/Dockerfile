FROM python:3.10

# Installer Git
RUN apt-get update && apt-get install -y git

WORKDIR /streamlit
#COPY requirements.txt ./requirements.txt
#RUN pip install streamlit 
#RUN pip install requests
#EXPOSE 8501
COPY application_sreamlit.py /streamlit
#ENTRYPOINT [ "streamlit", "run" ]
#CMD ["application_sreamlitpy"]#
# Commande par défaut pour exécuter l'application Streamlit
CMD ["python3", "-m", "streamlit", "run", "application_sreamlit.py", "--server.port", "8501"]

#CMD ["streamlit", "run", "application_sreamlit.py", "--server.port", "8501"]
