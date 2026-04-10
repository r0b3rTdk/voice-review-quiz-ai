import sounddevice as sd
import soundfile as sf

def record(audio_file="request_audio.wav"):
    print("OUVINDO...")

    # FORMATO DO AUDIO
    DURACAO_SEGUNDOS = 5.0    
    SAMPLE_RATE = 44100
    CANAIS = 1

    # COMECA A GRAVAR
    audio_data = sd.rec(
        int(DURACAO_SEGUNDOS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CANAIS
    )

    # ESPERA GRAVAR
    sd.wait()

    # SALVA EM .WAV
    sf.write(audio_file, audio_data, SAMPLE_RATE)

    return audio_file


    

    