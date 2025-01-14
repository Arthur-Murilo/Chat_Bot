while True:
    from bot.gemini import configure_gemini, response
    modelo = configure_gemini()
    prompt = input("Digite uma pergunta para que o Chat_Bot: ")
    print(response(modelo, prompt))