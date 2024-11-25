import cv2
import pytesseract
from transformers import pipeline
import sentencepiece



pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def extract_text_from_image(image_path):
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

# Chemin de votre image
image_path = '/Users/hajar/Documents/projet_img_txt/images_test/ob_a94ee4_demain-c-est-la-rentree-texte.jpg'

# Extraire le texte de l'image
texte_extrait = extract_text_from_image(image_path)

if texte_extrait:
    print("Texte extrait de l'image :")
    print(texte_extrait)
else:
    print("Aucun texte n'a été extrait de l'image.")


### Transformers ###

######### summarization ########
summarization = pipeline("summarization", model="moussaKam/barthez-orangesum-title")
print('résumé du texte :', summarization(texte_extrait))


##### Question reponse ######
#question_answerer = pipeline("question-answering", model="cmarkea/distilcamembert-base-qa",
     #tokenizer="cmarkea/distilcamembert-base-qa")

question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")


question_answerer(
    question="qui a terminé avant ?",
    context=texte_extrait,
)

print(question_answerer(
    question="qui a terminé avant ?",
    context=texte_extrait,
))

###Language Detection

from langdetect import detect
language = detect(texte_extrait)
print(f"Detected language: {language}")



##### Traduction #####
# Charger le modèle de traduction pré-entraîné
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

# Traduire la phrase du français vers l'anglais
translated_text = translator(texte_extrait, max_length=400)[0]['translation_text']

# Afficher la phrase traduite
print(f"Texte traduit : {translated_text}")


####
####Named Entity Recognition (NER)####
ner_pipeline = pipeline("ner", grouped_entities=True)
ner_results = ner_pipeline(texte_extrait)
print(ner_results)

##
### sentiment_analysis##
sentiment_analysis = pipeline("sentiment-analysis")
result = sentiment_analysis(texte_extrait)
print(result)

##
### text generation  ##
text_generator = pipeline("text-generation", model="gpt2")
generated_text = text_generator(texte_extrait, max_length=100)
print(generated_text)