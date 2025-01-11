import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

while True:
    from bot.gemini import configure_gemini, response
    modelo = configure_gemini()
    prompt = input("Digite uma pergunta para que o Chat_Bot: ")
    print(response(modelo, prompt))


