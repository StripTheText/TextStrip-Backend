# Dockerfile

# Verwenden eines offiziellen Python-Runtime-Images
FROM python:3.11

# Setzen des Arbeitsverzeichnisses in Docker
WORKDIR /usr/src/app

# Setzen einer Umgebungsvariable, um sicherzustellen, dass die Python-Ausgabe direkt im Terminal ohne Zwischenspeicherung ausgegeben wird
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Kopieren der Anforderungsdatei und Installieren der Abhängigkeiten
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren des restlichen Quellcodes in das Docker-Image
COPY . .

# Öffnen eines Ports
EXPOSE 8000

# Ausführen der App
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
