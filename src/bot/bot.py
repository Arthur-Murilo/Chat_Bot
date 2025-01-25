import google.generativeai as genai  # Biblioteca para interação com o GEMINI
from gtts import gTTS  # Biblioteca para conversão de texto em áudio


def configure_bot():
    api_key = "Sua chave API GEMINI"  # Chave da API do GEMINI
    if not api_key:  # Verifica se a Chave é valida
        raise ValueError("The GEMINI_API_KEY environment variable is not set.")
    genai.configure(api_key=api_key)  # Configura o GEMINI
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Você é um Assistente Virtual",  # Configuração de Modelo e Instrução de Sistema
    )


def response(model, prompt):  # Função para gerar Resposta
    resposta = model.generate_content(prompt, stream=True)  # Gera a resposta
    resposta.resolve()  # Finaliza a geração
    return resposta.text


def gerar_audio(resposta):  # Função para gerar Resposta como Audio
    audio = gTTS(text=resposta, lang="pt")  # Converte texto em áudio
    audio.save("src/media/resposta.mp3")  # Salva o áudio gerado
