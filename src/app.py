# Bibliotecas Utilizadas.
import ttkbootstrap as ttk
import os
from tkinter import Text, Scrollbar, PhotoImage, END, VERTICAL
from bot.bot import configure_bot, response, gerar_audio
from playsound import playsound


# Envia a mensagem e processa a resposta do chatbot
def send_message():
    user_input = user_entry.get()
    if user_input.strip():
        chatbot_response = response(modelo, user_input)
        response_text.config(state="normal")
        response_text.delete(1.0, END)
        response_text.insert("end", f"{chatbot_response}\n\n")
        response_text.see("end")
        response_text.config(state="disabled")
        user_entry.delete(0, END)

        # Gera o áudio da resposta e torna o botão visível
        gerar_audio(chatbot_response)
        escutar_button.pack(pady=10)


# Reproduz o áudio gerado pelo chatbot
def escutar_resposta():
    playsound("src/media/resposta.mp3")
    os.remove("src/media/resposta.mp3")

# Configuração inicial do modelo de IA
modelo = configure_bot()

# Configuração da interface gráfica
root = ttk.Window(themename="cosmo")
root.title("Assistente IA")
root.geometry("500x800")
root.wm_iconbitmap("assets/Icone.ico")

# Adiciona imagem de título
title_image = PhotoImage(file="assets/Image.png")
title_label = ttk.Label(root, image=title_image)
title_label.pack(pady=10)

# Campo de entrada e botão de envio
user_entry = ttk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(pady=20)
user_entry.focus()

send_button = ttk.Button(root, text="Enviar", command=send_message)
send_button.pack(pady=10)

# Área para exibir respostas com rolagem
frame = ttk.Frame(root)
frame.pack(expand=False, fill="both", padx=10, pady=10)

response_text = Text(frame, wrap="word", font=("Arial", 12), state="disabled")
response_text.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(frame, orient=VERTICAL, command=response_text.yview)
scrollbar.pack(side="right", fill="y")
response_text.configure(yscrollcommand=scrollbar.set)

# Botão para ouvir a resposta (inicialmente invisível)
escutar_button = ttk.Button(root, text="Escutar Resposta", command=escutar_resposta)

# Inicia o loop principal da interface
root.mainloop()
