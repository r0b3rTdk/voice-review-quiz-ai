# Referência: https://gist.github.com/korakot/c21c3476c024ad6d56d5f48b0bca92be
from audio_recorder import record
from transcriber import transcriber_audio
from quiz_engine import generate_question
from evaluator import evaluate

language = 'pt'
theme = input("Qual o tema? ")
question = generate_question(theme)
print(f"\nPergunta: {question}\n")

audio_file = record()
print(f"Audio salvo em {audio_file}")

texto = transcriber_audio(audio_file, language)
print(f"Audio transcrito {texto}")

evaluation = evaluate(theme, question, texto)
print(f"Avaliação: {evaluation}")