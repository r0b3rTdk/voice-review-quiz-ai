from openai import OpenAI

def generate_question(theme, level="facil"):
    client = OpenAI()

    prompt = f"""
    Gere 1 pergunta curta de revisão sobre o tema "{theme}".
    Nivel: {level}
    A pergunta deve ser objetiva, clara e boa para resposta oral.
    Não mostre a resposta. 
    """
    
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return response.output_text.strip()