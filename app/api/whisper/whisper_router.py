# Import of required Libraries
from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette.responses import PlainTextResponse, Response
import os
import tempfile
import whisper

router = APIRouter()

# Transcribe the Incoming Audio-File and send it back to the Front-End
whisper_model = whisper.load_model(
    name="base.en",
    download_root="app/models/whisper",
    in_memory=False
)


@router.post("/")
async def audio2text(file: UploadFile = File()):
    try:
        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)

        # Save the uploaded file to the temp file
        content = await file.read()
        temp_file.write(content)
        temp_file.close()

        # Load the Whisper model
        model = whisper.load_model("base")

        # Transcribe the audio file
        result = model.transcribe(temp_file.name)
        print(result)
        # Clean up the temp file
        os.unlink(temp_file.name)

        # Return the transcribed text as a plain text response
        return Response(content=result["text"], media_type="text/plain")

    except Exception as e:
        # Clean up the temp file in case of an error
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
        raise HTTPException(status_code=500, detail=str(e))
