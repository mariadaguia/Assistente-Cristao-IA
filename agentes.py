import os
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

# Configura a API Key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
MODEL_ID = "gemini-2.0-flash"

def gerar_resposta(prompt: str) -> str:
    model = genai.GenerativeModel(MODEL_ID)
    response = model.generate_content(prompt)
    return response.text.strip()

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Agente 1 - Selecionador de versículos
def agente_selecionador(sentimento, data_de_hoje):
    prompt = f"""
    Você é um assistente bíblico. seja sutil, Sua tarefa é encontrar até 3 versículos bíblicos que tragam apoio emocional com base no sentimento: '{sentimento}'.
    lembre-se que algummas sensações podem ser emocionais como a dor emocional pode ser classificada
    como um sentimento (como tristeza ou angústia), ou seja, o corpo sente algo físico, mas a causa podem vir das emoções
    foque em no maximo 3 versiculos relevantes com base
    no sentimento recebido para ajudar a lidar com esse sentimento. Dependendo do sentimento sugira versiculos para
    Acalmar, reduzir a ansiedade, ajudar a dormir, ou versiculos mais espirituais que Confortam, elevam a fé, trazem esperança,
    que levanta o ânimo, dá energia, traz alegria, versiculos motivacional	que Inspiram, fortalecem, ajudam em momentos difíceis. retorne apenas os versiculos biblicos

Data: {data_de_hoje}
Responda com os versículos.
"""
    return gerar_resposta(prompt)

# Agente 2 - Mensagem de conforto
def agente_confortador(sentimento, versiculos_buscados):
    prompt = f"""
Você é um psicólogo cristão. seja sutil, Com base na analise do sentimento '{sentimento}' e nos versículos abaixo, escreva uma resposta sutil, de apoio emocional e fé:
foque em respostas relevantes que podem ajudar a lidar com esse sentimento. Dependendo do sentimento sugira respostas para
Acalmar, reduzir a ansiedade, ajudar a dormir, ou versiculos espirituais, que Confortam, elevam a fé, trazem esperança,
versiculos motivacional que Inspiram, fortalecem, ajudam em momentos difíceis sobre ele. lembre-se que algummas sensações podem ser emocionais
como a dor emocional pode ser classificada como um sentimento (como tristeza ou angústia), ou seja, o corpo sente algo físico, mas a causa podem vir das emoções.

Versículos:
{versiculos_buscados}
"""
    return gerar_resposta(prompt)

# Agente 3 - Louvores sugeridos
def agente_buscador_louvores(sentimento, msg_conforto, versiculos_buscados):
    prompt = f"""
Você é um assistente musical cristão. Sugira até 3 louvores (músicas gospel) com base no sentimento '{sentimento}', nos versículos e na mensagem de conforto abaixo.

Versículos:
{versiculos_buscados}

Mensagem de conforto:
{msg_conforto}

Os louvores devem ser relevantes emocionalmente e espiritualmente.
"""
    return gerar_resposta(prompt)

# Agente 4 - Notas musicais
def agente_musicoterapeuta(sentimento, msg_conforto, louvores_buscados):
    prompt = f"""
    Você é um musicoterapeuta cristão. Com base no sentimento '{sentimento}', na mensagem de conforto e nos louvores abaixo, gere uma sequência de exatamente 32 notas musicais, separadas por vírgula. Cada nota deve estar no formato padrão ocidental: Cada nota deve usar uma das letras musicais: A, B, C, D, E, F ou G. (com ou sem # ou b), seguida de um número entre 2 e 7 indicando a oitava.

    ⚠️ Só use as notas válidas da tabela abaixo:
    - C, C#, Db
    - D, D#, Eb
    - E, Fb
    - F, E#, F#, Gb
    - G, G#, Ab
    - A, A#, Bb
    - B, Cb

    Exemplos válidos: C4, D#5, Bb3, F#6

    ❌ Não inclua números isolados, textos, explicações ou notas fora da escala.
    Mensagem de conforto:

{msg_conforto}

Louvores:
{louvores_buscados}

Não inclua explicações. Apenas a lista de notas, com variação melódica e sem repetições excessivas.
"""
    return gerar_resposta(prompt)
