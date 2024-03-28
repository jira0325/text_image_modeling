from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL de votre API FastAPI
API_URL = "http://localhost:8000"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-data', methods=['GET'])
def get_data():
    response = requests.get(f"{API_URL}/get-data")
    if response.status_code == 200:
        return response.json()
    else:
        return "Erreur lors de la récupération des données de l'API."

@app.route('/get-summarization', methods=['GET'])
def get_summarization():
    response = requests.get(f"{API_URL}/get-summarization")
    if response.status_code == 200:
        return response.json()
    else:
        return "Erreur lors de la récupération de la résumé de l'API."

@app.route('/question-answer', methods=['POST'])
def question_answer():
    quest = request.form['quest']
    response = requests.post(f"{API_URL}/api/v1/question", json={"quest": quest})
    if response.status_code == 200:
        return response.json()
    else:
        return "Erreur lors de la récupération de la réponse à la question."

@app.route('/get-translation', methods=['GET'])
def get_translation():
    response = requests.get(f"{API_URL}/get-translation")
    if response.status_code == 200:
        return response.json()
    else:
        return "Erreur lors de la récupération de la traduction de l'API."

if __name__ == '__main__':
    app.run(debug=True)
