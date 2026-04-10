import os
from openai import OpenAI

def transcriber_audio(audio_file, language = "pt"):
    # CRIACAO DO CLIENTE
    client = OpenAI()

    # ABRIR O ARQUIVO
    with open(audio_file, "rb") as file:
        # MANDA O AUDIO PARA TRANSCRICAO
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=file,
            language=language
        )
    
    # RETORNA O AUDIO TRANSCRITO EM TEXTO
    return transcription.text