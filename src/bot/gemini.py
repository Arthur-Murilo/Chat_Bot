from dotenv import load_dotenv
import os 
import google.generativeai as genai

load_dotenv()

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("The GEMINI_API_KEY environment variable is not set.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name="gemini-1.5-flash",
    system_instruction="Você é um espanhol e traduz tudo que eu falar para espanhol"
    )                             

def response(model, prompt):
    resposta = model.generate_content(prompt, stream=True)
    resposta.resolve()
    return resposta.text
    