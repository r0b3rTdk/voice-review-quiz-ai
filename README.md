# Quiz Oral de Revisão por Voz com IA

Projeto em Python que gera uma pergunta de revisão com IA, grava a resposta do usuário por voz, transcreve o áudio e avalia a resposta com feedback curto.

## Funcionalidades

- gerar pergunta com base em um tema
- gravar resposta em áudio
- transcrever áudio para texto
- avaliar a resposta com IA

## Tecnologias

- Python
- OpenAI API
- sounddevice
- soundfile

## Estrutura

```bash
.
├── main.py
├── audio_recorder.py
├── transcriber.py
├── quiz_engine.py
└── evaluator.py
```

## Instalação

```bash
pip install openai sounddevice soundfile
```

## Configuração

Defina sua chave da OpenAI como variável de ambiente.

### PowerShell

```powershell
$env:OPENAI_API_KEY="sua_chave_aqui"
```

## Execução

```bash
python main.py
```

## Autor

Projeto desenvolvido por **Robert Emanuel**.
