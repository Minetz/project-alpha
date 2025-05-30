import os
from tempfile import NamedTemporaryFile

def transcribe_audio(client, audio_bytes):
    with NamedTemporaryFile(delete=False, suffix=".m4a") as audio_temp:
        audio_temp.write(audio_bytes)
        audio_temp.flush()
        audio_temp_path = audio_temp.name

    with open(audio_temp_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="verbose_json",
            timestamp_granularities=["word"],
            prompt="Trascrivi in Italiano. Trattiamo una seduta di terapia tra un terapeuta e un paziente."
        )

    os.remove(audio_temp_path)
    return transcription