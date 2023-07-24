# Laden von Bibliotheken
from fastapi import Depends, APIRouter
from api.summarizer.api_models import SummarizeInputObject, SummarizeOutputObject
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from rouge import Rouge

# Definiere eine globale Variable für das Modell
summarization_pipeline = None
summarization_tokenizer = None
summarization_model = None

# Definiere einen neuen Router (APIRouter)
summarization_router = APIRouter(
    prefix="/summarizer",
    responses={404: {"description": "Not found"}},
    dependencies=[]
)


# Definiere was beim Start der Anwendung passieren soll
@summarization_router.on_event("startup")
def on_startup():
    """
    Loads the classification model
    """
    load_pipeline_summarization()
    load_model_summarization()


def load_pipeline_summarization():
    """
    Loads the summarization_pipeline from the given path to a global variable
    """
    # Hole die globale Variable
    global summarization_pipeline
    # Lade das Modell zu die globale Variable
    summarization_pipeline = pipeline("summarization", model="tkister/autotrain-news-paper-75687140071")


def load_model_summarization():
    """
    Loads the summarization model from the given path to a global variable
    """
    # Hole die globale Variable
    global summarization_tokenizer
    global summarization_model
    # Lade das Modell zu die globale Variable
    summarization_tokenizer = AutoTokenizer.from_pretrained("tkister/autotrain-news-paper-75687140071")
    summarization_model = AutoModelForSeq2SeqLM.from_pretrained("tkister/autotrain-news-paper-75687140071")


# Funktion, die das Modell zurückgibt
def get_pipeline_summarization() -> pipeline:
    """
    Returns the summarization pipeline
    """
    # Hole die globale Variable
    global summarization_pipeline
    return summarization_pipeline


# Funktion, die Tokenizer und Modell zurückgibt
def get_model_summarization() -> (AutoTokenizer, AutoModelForSeq2SeqLM):
    """
    Returns the summarization model
    """
    # Hole die globale Variable
    global summarization_tokenizer
    global summarization_model
    return summarization_tokenizer, summarization_model


# Definiere einen Endpunkt für die Klassifizierung
@summarization_router.post("/")
async def summarize_text_pipline(
        InputObject: SummarizeInputObject,
        sum_pipeline: pipeline = Depends(get_pipeline_summarization)) -> SummarizeOutputObject:
    """
    Summarize the given text using the given model
    """
    # Length of input text
    length_of_input = len(InputObject.text)
    # Max Length of output text
    sum_pipeline.max_length = int(length_of_input * (1 - InputObject.compression_rate))
    # Min Length of output text
    sum_pipeline.min_length = int((length_of_input * (1 - InputObject.compression_rate)) - 30)
    # Text to summarize
    input_txt = f'summarize the text with min: {int((length_of_input * (1 - InputObject.compression_rate)) - 30)} words: ' + InputObject.text
    # Summarize the text
    summary = sum_pipeline(input_txt)
    # Return the summary
    return SummarizeOutputObject(
        summary=summary[0]['summary_text'],
        input_word_count=length_of_input,
        summary_word_count=len(summary[0]['summary_text']),
        input_compression_rate=InputObject.compression_rate,
        real_compression_rate=len(summary[0]['summary_text']) / length_of_input
    )


@summarization_router.post("/compress")
async def summarize_text_model(
        InputObject: SummarizeInputObject,
        model_object=Depends(get_model_summarization)
) -> SummarizeOutputObject:
    """
    Summarize the given text using the given model
    :param InputObject: Object with text and compression rate
    :param model_object: Object with tokenizer and model
    :return:
    """

    # Auspacken der Modellobjekte
    tokenizer, model = model_object
    # Definition of variables
    summ_ready = False
    counter = 0
    input_help = InputObject.text
    summary_text = ""
    # Loop for summarization
    while counter < 20 and summ_ready is False:
        # Tokenize the input text
        inputs = tokenizer([input_help], max_length=1024, truncation=True, padding='longest', return_tensors='pt')
        # Generate the summary
        summary_pre = model.generate(inputs['input_ids'], num_beams=4, max_length=1024, early_stopping=True)
        # Decode the summary
        summary_text = tokenizer.decode(summary_pre[0], skip_special_tokens=True)
        # Check if the summary is ready
        if len(summary_text) > 0 and (len(summary_text) / len(InputObject.text)) < InputObject.compression_rate:
            summ_ready = True
        else:
            counter += 1
            input_help = summary_text
    # Return the summary
    return SummarizeOutputObject(
        summary=summary_text,
        input_word_count=len(InputObject.text),
        summary_word_count=len(summary_text),
        input_compression_rate=InputObject.compression_rate,
        real_compression_rate=len(summary_text) / len(InputObject.text)
    )
