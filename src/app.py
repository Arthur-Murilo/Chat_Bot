import ttkbootstrap as ttk
import os
from tkinter import Text, Scrollbar, PhotoImage, END, VERTICAL
from bot.bot import configure_bot, response, gerar_audio
from playsound import playsound

# Função para enviar a mensagem
def send_message():
    user_input = user_entry.get()
    if user_input.strip():
        chatbot_response = response(modelo, user_input)
        response_text.config(state="normal")
        response_text.delete(1.0, END)
        response_text.insert("end", f"Você: {user_input}\n\n")  # Exibe a entrada do usuário
        response_text.insert("end", f"{chatbot_response}\n\n")  # Exibe a resposta do chatbot
        response_text.see("end")  # Move a rolagem para o final do texto
        response_text.config(state="disabled")  # Torna o Text apenas leitura
        user_entry.delete(0, END)  # Limpa o campo de entrada
        
        # Gerar o áudio
        os.remove('src/media/resposta.mp3')
        gerar_audio(chatbot_response)
        # Adicionar o botão de escutar resposta
        escutar_button.pack(pady=10)  # Torna o botão visível

# Função para escutar a resposta do chatbot
def escutar_resposta():
    playsound("src/media/resposta.mp3")  # Reproduz o áudio gerado

# Configuração inicial do modelo
modelo = configure_bot()

# Criação da janela principal
root = ttk.Window(themename="cosmo")
root.title("Assistente IA")
root.geometry("500x800")

icon_path = "assets/Icone.ico"  # Caminho para o arquivo de ícone
root.wm_iconbitmap(icon_path)

# Adicionando uma imagem no topo
title_image = PhotoImage(file="assets/Image.png")
title_label = ttk.Label(root, image=title_image)
title_label.pack(pady=10)

# Campo de entrada para a pergunta do usuário
user_entry = ttk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(pady=20)
user_entry.focus()

# Botão para enviar a pergunta
send_button = ttk.Button(root, text="Enviar", command=send_message)
send_button.pack(pady=10)

# Frame para o Text e Scrollbar
frame = ttk.Frame(root)
frame.pack(expand=False, fill="both", padx=10, pady=10)

# Widget de texto para exibir as respostas
response_text = Text(frame, wrap="word", font=("Arial", 12), state="disabled")
response_text.pack(side="left", fill="both", expand=True)

# Scrollbar para o Text
scrollbar = Scrollbar(frame, orient=VERTICAL, command=response_text.yview)
scrollbar.pack(side="right", fill="y")

response_text.configure(yscrollcommand=scrollbar.set)

# Botão "Escutar Resposta" (inicialmente invisível)
escutar_button = ttk.Button(root, text="Escutar Resposta", command=escutar_resposta)

# Iniciar o loop principal da interface gráfica
root.mainloop()
