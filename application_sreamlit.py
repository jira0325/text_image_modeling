import streamlit as st
import requests

# Lien vers votre image Docker sur Docker Hub
DOCKER_HUB_URL = "https://hub.docker.com/r/votre_utilisateur/votre_image"

# Variable globale pour stocker le texte extrait
extracted_text = None

# Fonction pour extraire le texte de l'image via votre API FastAPI
def extract_text(image):
    global extracted_text
    files = {"image": image}
    response = requests.get(f"{DOCKER_HUB_URL}/get_text", files=files)
    if response.status_code == 200:
        extracted_text = response.json()
        return extracted_text
    else:
        return "Erreur lors de l'extraction du texte"

# Fonction pour obtenir un résumé du texte via votre API FastAPI
def summarize_text(text):
    response = requests.get(f"{DOCKER_HUB_URL}/summarization", params={"text": text})
    if response.status_code == 200:
        return response.json()
    else:
        return "Erreur lors de la génération du résumé"

# Fonction pour obtenir une réponse à une question via votre API FastAPI
def get_answer(question, context):
    data = {"quest": question}
    response = requests.post(f"{DOCKER_HUB_URL}/api/v1/question", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return "Erreur lors de la génération de la réponse"

# Fonction pour traduire le texte via votre API FastAPI
def translator(text):
    response = requests.get(f"{DOCKER_HUB_URL}/get-translation", params={"text": text})
    if response.status_code == 200:
        return response.json()["translation"]
    else:
        return "Erreur lors de la traduction du texte"


# Page d'accueil de l'application Streamlit
def home():
    st.title("Application Image-Texte")
    st.write("Téléchargez une image pour extraire le texte et effectuer des opérations sur celui-ci.")

    uploaded_image = st.file_uploader("Télécharger une image", type=["jpg", "png"])
    if uploaded_image is not None:
        text = extract_text(uploaded_image)
        st.write("Texte extrait de l'image:")
        st.write(text)
        
        # Options pour les opérations sur le texte
        option = st.selectbox("Opérations sur le texte", ["Traduction", "Question/Réponse", "Résumé"])
        if option == "Traduction":
            translated_text = translator(extracted_text)
            st.write("Texte traduit:")
            st.write(translated_text)
        elif option == "Question/Réponse":
            question = st.text_input("Posez votre question")
            if st.button("Obtenir la réponse"):
                answer = get_answer(question, extracted_text)
                st.write("Réponse à la question:")
                st.write(answer)
        elif option == "Résumé":
            summarized_text = summarize_text(extracted_text)
            st.write("Résumé du texte:")
            st.write(summarized_text)


# Lancer l'application Streamlit
if __name__ == "__main__":
    home()
