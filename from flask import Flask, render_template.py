from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL de l'API déployée
API_URL = "http://localhost:8000/api/v1/question"  # Mettez ici l'URL de votre API déployée

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = request.form['input_data']

        # Appel de l'API déployée pour obtenir la prédiction
        response = requests.post(API_URL, json={'input_data': input_data})

        if response.status_code == 200:
            prediction = response.json()['prediction']
            return render_template('index.html', prediction=prediction)
        else:
            return "Erreur lors de l'appel à l'API"

if __name__ == '__main__':
    app.run(debug=True)
