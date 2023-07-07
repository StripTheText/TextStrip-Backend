# Laden von Bibliotheken
import pathlib

import pandas as pd
import tensorflow as tf

from fastapi import Depends, APIRouter
from api.classifier.api_models import ClassifyInputObject, ClassifyOutputObject

# Definieren von Konstanten und Pfaden
REPOSITORY_ROOT_PATH = pathlib.Path(__file__).parent.parent.parent
MODELS_PATH = REPOSITORY_ROOT_PATH.joinpath("models")
CLASSIFICATION_MODEL_PATH = MODELS_PATH.joinpath("classifier", "classification_rnn_2.0")

# Definiere eine globale Variable für das Modell
classification_model = None

# Definiere einen neuen Router (APIRouter)
classifier_router = APIRouter(
    prefix="/classifier",
    responses={404: {"description": "Not found"}},
    dependencies=[]
)


# Definiere was beim Start der Anwendung passieren soll
@classifier_router.on_event("startup")
def load_model_Classification():
    """
    Loads the classification model from the given path to a global variable
    """
    # Hole die globale Variable
    global classification_model
    # Lade das Modell zu die globale Variable
    classification_model = tf.keras.models.load_model(
        filepath=CLASSIFICATION_MODEL_PATH,
        compile=True,
        custom_objects=None,
        options=None
    )


# Funktion, die das Modell zurückgibt
def get_model_classification() -> tf.keras.models.Model:
    """
    Returns the classification model
    """
    global classification_model
    return classification_model


# Definiere einen Endpunkt für die Klassifizierung
@classifier_router.post("/")
async def classify_text(
        text: ClassifyInputObject,
        model: tf.keras.models.Model = Depends(get_model_classification)) -> ClassifyOutputObject:
    """
    Classifies the given text using the given model
    """
    # Definiere die Labels
    LABELS: list[str] = ["Blog", "Book", "News", "Paper", "Review"]
    prediction = model.predict(pd.DataFrame([text.text]))
    return ClassifyOutputObject(outputClass=LABELS[prediction.argmax(axis=1)[0]])
