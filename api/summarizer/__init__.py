# Laden von Bibliotheken
import pathlib

import pandas as pd
import tensorflow as tf

from fastapi import Depends, APIRouter
from api.summarizer.api_models import SummarizeInputObject, SummarizeOutputObject

# Definieren von Konstanten und Pfaden
REPOSITORY_ROOT_PATH = pathlib.Path(__file__).parent.parent.parent
MODELS_PATH = REPOSITORY_ROOT_PATH.joinpath("models")
SUMMARIZATION_MODEL_PATH = MODELS_PATH.joinpath("classifier", "classification_rnn_2.0")

# Definiere eine globale Variable für das Modell
summarization_model = None

# Definiere einen neuen Router (APIRouter)
summarization_router = APIRouter(
    prefix="/summarizer",
    responses={404: {"description": "Not found"}},
    dependencies=[]
)


# Definiere was beim Start der Anwendung passieren soll
@summarization_router.on_event("startup")
def load_model_summarization():
    """
    Loads the classification model from the given path to a global variable
    """
    # Hole die globale Variable
    global summarization_model
    # Lade das Modell zu die globale Variable
    summarization_model = tf.keras.models.load_model(
        filepath=SUMMARIZATION_MODEL_PATH,
        compile=True,
        custom_objects=None,
        options=None
    )


# Funktion, die das Modell zurückgibt
def get_model_summarization() -> tf.keras.models.Model:
    """
    Returns the classification model
    """
    global summarization_model
    return summarization_model


# Definiere einen Endpunkt für die Klassifizierung
@summarization_router.post("/")
async def summarize_text(
        InputObject: SummarizeInputObject,
        model: tf.keras.models.Model = Depends(get_model_summarization)) -> SummarizeOutputObject:
    """
    Summarize the given text using the given model
    """
    summary = model.predict(pd.DataFrame([InputObject.text]))
    pass
