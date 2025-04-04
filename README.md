## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
---
# 🧠 Chatbot Assistente IA

Este projeto é um chatbot com interface gráfica que utiliza a biblioteca **Google Generative AI** (GEMINI) para gerar respostas inteligentes a partir de prompts fornecidos pelo usuário. Além disso, ele converte as respostas geradas em áudio usando a biblioteca **gTTS** (Google Text-to-Speech).

---

## 📁 Estrutura do Projeto

A organização dos arquivos do projeto segue a seguinte estrutura:
```
Projeto/
│
├── src/
│   ├── bot/
│   │   └── bot.py            # Configuração do modelo GEMINI e funções do chatbot
│   ├── media/
│   │   └── resposta.mp3      # Áudios gerados pelo chatbot
│   └── app.py                # Código principal da interface gráfica
│
├── assets/
│   ├── Icone.ico             # Ícone para a janela da interface
│   └── Image.png             # Imagem exibida no topo da interface
│
└── README.md                 # Arquivo de documentação
```

---

## 🚀 Funcionalidades

1. **Geração de Respostas Inteligentes**
   - Utiliza o modelo generativo **GEMINI** para responder a mensagens enviadas pelo usuário.

2. **Conversão de Respostas para Áudio**
   - As respostas são convertidas para áudio e salvas como arquivos `.mp3` na pasta `src/media`.

3. **Interface Gráfica Amigável**
   - Desenvolvida com **Tkinter** e estilizada com **ttkbootstrap**, a interface oferece uma experiência fluida e intuitiva para o usuário.

4. **Reprodução de Áudio**
   - Um botão permite ouvir as respostas geradas diretamente pela interface.

---

## 📜 Como Funciona

### **Arquivo `bot.py`**
Local: `src/bot/bot.py`
Este arquivo é responsável por:
- Configurar o modelo GEMINI através da função `configure_bot()`.
- Gerar respostas com a função `response()`.
- Converter as respostas em áudio usando a função `gerar_audio()`.

### **Arquivo `app.py`**
Local: `src/app.py`
Este arquivo define a interface gráfica do chatbot:
- Cria campos para entrada de texto do usuário e exibição das respostas.
- Usa a função `send_message()` para processar mensagens, gerar respostas e exibir na interface.
- Reproduz áudios gerados com a função `escutar_resposta()`.

### **Recursos Adicionais**
- **Pasta `assets/`**: Contém arquivos visuais, como o ícone da janela (`Icone.ico`) e a imagem exibida na interface (`Image.png`).
- **Pasta `src/media/`**: Armazena os arquivos de áudio `.mp3` gerados a partir das respostas do chatbot.

---

## 🛠️ Pré-requisitos

Antes de executar o projeto, instale as dependências necessárias:
```bash
pip install ttkbootstrap google-generativeai gtts playsound
```
Ou utilizando o requeriments.txt:
```bash
pip install -r requirements.txt
```
---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/chatbot-assistente-ia.git
   cd chatbot-assistente-ia
   ```

2. Configure sua chave API GEMINI no código (`bot.py`):
   ```python
   api_key = "Sua chave API GEMINI"
   ```

3. Execute o arquivo principal:
   ```bash
   python src/app.py
   ```

---

## 🎨 Interface Gráfica

- **Entrada de Mensagens**: Campo para digitar perguntas ou comandos para o chatbot.
- **Exibição de Respostas**: Área que mostra a resposta gerada pelo chatbot.
- **Botão "Escutar Resposta"**: Reproduz o áudio gerado da resposta.

---

## 💡 Tecnologias Utilizadas

- **Google Generative AI (GEMINI)**: Para geração de respostas inteligentes.
- **gTTS (Google Text-to-Speech)**: Para conversão de texto em áudio.
- **Tkinter e ttkbootstrap**: Para construção e estilização da interface gráfica.
- **Playsound**: Para reprodução dos áudios gerados.

---

## 📌 Notas

- Certifique-se de que a chave API GEMINI esteja correta e ativa.
- O áudio gerado é salvo automaticamente em `src/media/resposta.mp3` e sobrescrito a cada nova mensagem.

---

## ✉️ Contato

Se tiver dúvidas ou sugestões, entre em contato:
- **Nome**: Arthur
- **E-mail**: [arthur.msc1811@hotmail.com](mailto:arthur.msc1811@hotmail.com)
- **LinkedIn**: [linkedin.com/in/arthur-santos-engineerml](https://linkedin.com/in/arthur-santos-engineerml)

