# Import of required Libraries
from fastapi import APIRouter
from pydantic import BaseModel
import tensorflow as tf


class SummarizationIntputObject(BaseModel):
    compressionRate: float = 0.5
    summarizationInput: str | None = None


class SummarizationOutputObject(BaseModel):
    summarization: str | None = None


router = APIRouter()


# Summarize the incoming Text[str] -> Class[str]
@router.post("/")
async def summarize_text(sumInput: SummarizationIntputObject):
    print(sumInput)
