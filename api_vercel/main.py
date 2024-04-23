from fastapi import FastAPI , UploadFile, File, Depends
import cv2
import pytesseract
from transformers import pipeline
import sentencepiece
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List, Optional 
import numpy as np
from fastapi.responses import StreamingResponse
import io
import re
import uvicorn


api = FastAPI(
    title='Image-Texte'
)

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

class User(BaseModel):
    id: Optional[UUID] = uuid4() 
    first_name: str
    password : str

# Fonction pour extraire le texte de l'image
def get_image(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if image is None:
        print("Impossible de charger l'image.")
        return None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    blur = cv2.GaussianBlur(thresh, (5, 5), 0)
    texte = pytesseract.image_to_string(blur)
    return texte

image_content = None  # Variable globale pour stocker le contenu de l'image

@api.post('/get-data')
async def get_data(image: UploadFile = File(...)):
    global image_content
    image_content = await image.read()
    # Traiter l'image comme requis
    return {"message": "Image téléchargée avec succès."}

def remove_special_characters(text):
    # Utilisation d'une expression régulière pour remplacer les caractères spéciaux par une chaîne vide
    cleaned_text = re.sub(r'[^\w\s]', ' ', text)
    return cleaned_text

@api.get('/get_text')
async def get_text():
    if image_content is None:
        return {"error": "Aucune image n'a été téléchargée."}
    text = get_image(image_content)
    texte_sans_n = remove_special_characters(text)
    texte_sans_n = text.replace('\n', ' ')
    return {"text":texte_sans_n}


# Route GET pour la summarization du texte extrait
@api.get('/summarization')
def summarize_text():
    # Obtenir le texte extrait de l'image via la route POST

    if image_content is None:
        return {"error": "Aucune image n'a été téléchargée."}
    text = get_image(image_content)
    texte_sans_n = text.replace('\n', '')
    summarization = pipeline("summarization", model="moussaKam/barthez-orangesum-title")
    summarized_text = summarization(texte_sans_n)
    
    return summarized_text

   

### question anwrer ###
class Title(BaseModel):
    
    quest: str

def question_answerer(quest):
    if image_content is None:
        return {"error": "Aucune image n'a été téléchargée."}
    text = get_image(image_content)

    question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    result_question = question_answerer(
    question= quest,
    context=text,
    )
    return {'answer' :  result_question}



@api.post("/api/v1/question")
def create_question(user : Title):
 #db.append(user)
 #get_recommendations(movie)
 return question_answerer(user.quest)
  

#### translation ###
@api.get('/get-translation')
def translator():
    if image_content is None:
        return {"error": "Aucune image n'a été téléchargée."}
    text = get_image(image_content)

    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    translated_text = translator(text, max_length=400)[0]['translation_text']
    return {'translation':  translated_text}


if __name__ == "__main__":
    uvicorn.run("main:api", host="127.0.0.1", port=8000, reload=True)


    