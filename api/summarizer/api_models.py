# Laden von Bibliotheken
from pydantic import BaseModel


# Definiere eine Klasse, die die Eingabe der API beschreibt
class SummarizeInputObject(BaseModel):
    compression_rate: float | None = 0.5
    text: str | None = None


# Definiere eine Klasse, die die Ausgabe der API beschreibt
class SummarizeOutputObject(BaseModel):
    summary: str | None = None
    input_word_count: int | None = None
    summary_word_count: int | None = None
    input_compression_rate: float | None = None
    real_compression_rate: float | None = None

