from openai import OpenAI

def evaluate(theme, question, answer):
    client = OpenAI()

    prompt = f"""
    Você é um avaliador de quiz oral de revisão.
    O tema é: {theme}
    A pergunta foi: {question}
    A resposta do aluno foi: {answer}

    Classifique como: correta, parcial ou incorreta.
    Dê feedback curto, claro e didático.
    Não invente conteúdo desnecessário.
    Não faça resposta longa.
    """

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return response.output_text.strip()