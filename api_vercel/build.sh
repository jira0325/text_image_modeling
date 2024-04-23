python3.11.0 -m venv venv
source venv/bin/activate
#source venv/bin/activate
uvicorn main:api --host 0.0.0.0 --port 8080
#pip install -r requirements.txt