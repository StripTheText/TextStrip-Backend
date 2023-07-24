# Laden von Bibliotheken
from pydantic import BaseModel


# Definiere eine Klasse, die die Ausgabe der API beschreibt
class ClassifyInputObject(BaseModel):
    text: str | None = None


# Definiere eine Klasse, die die Ausgabe der API beschreibt
class ClassifyOutputObject(BaseModel):
    outputClass: str | None = None
