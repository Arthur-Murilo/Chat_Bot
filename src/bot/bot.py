from dotenv import load_dotenv
import os 
import google.generativeai as genai
from gtts import gTTS

load_dotenv()

def configure_bot():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("The GEMINI_API_KEY environment variable is not set.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name="gemini-1.5-flash",
    system_instruction="Você é um chatbot"                            
    )                             

def response(model, prompt):
    resposta = model.generate_content(prompt, stream=True)
    resposta.resolve()
    return resposta.text

def gerar_audio(respota):
    audio = gTTS(text=respota, lang='pt')
    audio.save('src/media/resposta.mp3')
