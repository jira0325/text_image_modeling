FROM python:3.10

# Installer Git
RUN apt-get update && apt-get install -y git

WORKDIR /streamlit
#COPY requirements.txt ./requirements.txt
#RUN pip install -r requirements.txt
EXPOSE 8501
COPY application_sreamlit.py /streamlit
ENTRYPOINT [ "streamlit", "run" ]
CMD ["application_sreamlitpy"]
