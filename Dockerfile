# Dockerfile für Streamlit-App
# Ziehen des Basisimages von Docker Hub
FROM python:3.11-slim

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie den Projektcode in den Container
COPY ./requirements.txt /app/requirements.txt

# Installieren Sie die benötigten Python-Pakete
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Herunter Laden des Huggingface Modells
RUN python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; AutoTokenizer.from_pretrained('tkister/autotrain-news-paper-75687140071');AutoModelForSeq2SeqLM.from_pretrained('tkister/autotrain-news-paper-75687140071')"

# Kopieren Sie den Projektcode in den Container
COPY . /app

# Exponieren Sie den Port, auf dem die Fast-Api läuft
EXPOSE 8080

# Wie soll der Container gestartet werden?
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
