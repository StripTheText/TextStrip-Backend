# Import of required Libraries
from fastapi import APIRouter
from pydantic import BaseModel
import tensorflow as tf


class ClassifyInputObject(BaseModel):
    inputText: str | None = None


class ClassifyOutputObject(BaseModel):
    outputClass: str | None = None


router = APIRouter()


# Classify the incoming Text[str] -> Class[str]
@router.post("/")
async def classify_text(inputObject: ClassifyInputObject):
    model = tf.keras.models.load_model("app/models/classifier/classification_rnn_1.0")
    print(model.summary())
    print(inputObject.inputText)

