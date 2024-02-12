from fastapi import FastAPI
import cv2
import pytesseract
from transformers import pipeline
import sentencepiece
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List, Optional 



api = FastAPI(
    title='Image-Texte'
)

class User(BaseModel):
    id: Optional[UUID] = uuid4() 
    first_name: str
    password : str

def get_image(image_path):
    # Charger l'image avec OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("Impossible de charger l'image.")
        return None

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un seuillage pour obtenir un texte plus clair
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Appliquer un flou pour améliorer la qualité de l'OCR
    blur = cv2.GaussianBlur(thresh, (5, 5), 0)

    # Utilisation de Tesseract pour l'extraction du texte
    texte = pytesseract.image_to_string(blur)

    return texte


def get_extract_text_from_image():
    # Chemin de votre image
    image_path = '/Users/hajar/Documents/projet_img_txt/images_test/ob_a94ee4_demain-c-est-la-rentree-texte.jpg'

    # Extraire le texte de l'image
    texte_extrait = get_image(image_path)

    if texte_extrait:
        #print("Texte extrait de l'image :")
        return texte_extrait
    else:
        return "Aucun texte n'a été extrait de l'image."

@api.get('/get-data')
def get_data():
    text = get_extract_text_from_image()
    return text

texte_extrait = get_data()

@api.get('/get-summarization')
def get_summarization():
    summarization = pipeline("summarization", model="moussaKam/barthez-orangesum-title")
    return summarization(texte_extrait)


### question anwrer ###
class Title(BaseModel):
    
    quest: str

def question_answerer(quest):
    question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    result_question = question_answerer(
    question= quest,
    context=texte_extrait,
    )
    return result_question



@api.post("/api/v1/question")
def create_question(user : Title):
 #db.append(user)
 #get_recommendations(movie)
 return question_answerer(user.quest)
  

#### translation ###
@api.get('/get-translation')
def translator():
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    translated_text = translator(texte_extrait, max_length=400)[0]['translation_text']
    return  translated_text





    