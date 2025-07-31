# 🤖 Chatbot Educacional para TEA

Este é um **chatbot educacional desenvolvido com Flask** voltado especialmente para auxiliar pessoas com **Transtorno do Espectro Autista (TEA)**. Ele utiliza o modelo **LLaMA 3.3 70B** via [Together API](https://www.together.ai/) para gerar respostas em linguagem natural.

---

## 🎯 Objetivo

Oferecer uma ferramenta digital simples, acessível e empática para auxiliar o aprendizado e a comunicação de pessoas com TEA, por meio de uma interface web clara e intuitiva.

---

## 📸 Preview da Interface

A interface web é responsiva e utiliza um layout limpo com balões de conversa:

> ⚠️ Adicione aqui um screenshot caso deseje.

<img width="1914" height="974" alt="image" src="https://github.com/user-attachments/assets/0170bcce-71ad-4b8d-b335-9b74c1ed3217" />


## 🚀 Tecnologias Utilizadas

- Python 3
- Flask + Flask-CORS
- Together API (LLaMA 3.3)
- HTML + CSS + JavaScript puro
- Gunicorn (para produção)
- Render ou Heroku (para deploy)
- dotenv (variáveis de ambiente)

---

## 📁 Estrutura do Projeto

```bash
/
├── TesteServidorFlask.py       # Backend em Flask (servidor principal)
├── index.html                  # Frontend (interface do chatbot)
├── requirements.txt            # Dependências do Python
├── Procfile                    # Configuração para deploy
├── .env.example                # Exemplo de variáveis de ambiente
└── templates/
    └── index.html              # Template usado pelo Flask
