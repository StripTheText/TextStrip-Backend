from fastapi import FastAPI, Depends, APIRouter
from pydantic import BaseModel
import pandas as pd
import tensorflow as tf

app = FastAPI()

model_classification = None
model_summarization = None


class ClassifyOutputObject(BaseModel):
    outputClass: str | None = None


# Diese Funktion wird ausgeführt, wenn die Anwendung startet
@app.on_event("startup")
def load_models():
    global model_classification
    global model_summarization
    # Pfad zu deinem TensorFlow Modells
    model_classification = tf.keras.models.load_model("models/classification_rnn_2.0")
    model_summarization = tf.keras.models.load_model("models/classification_rnn_2.0")


# Du kannst eine Abhängigkeit erstellen, die das Modell bereitstellt
def get_model_classification():
    return model_classification


def get_model_summarization():
    return model_summarization


@app.post("/api/classification")
async def classify_text(text: str, model: tf.keras.models.Model = Depends(get_model_classification)):
    """
    Classifies the given text using the given model
    """
    labels: list[str] = ["blog", "book", "news", "paper", "review"]
    prediction = model.predict([pd.DataFrame([text])])
    return ClassifyOutputObject(outputClass=labels[prediction.argmax(axis=1)[0]])


@app.post("/api/summarization")
async def summarize_text(text: str, compression_rate: float = 0.5,
                         model: tf.keras.models.Model = Depends(get_model_summarization)):
    """
    Summarizes the given text using the given compression rate
    """
    pass
