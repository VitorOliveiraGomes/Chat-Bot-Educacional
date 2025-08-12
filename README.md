# Chatbot Educacional para Pessoas com TEA

Este é um chatbot web feito com Flask + Together AI, projetado para auxiliar pessoas no espectro autista a estudar de forma clara, acolhedora e acessível.

## Funcionalidades

- Login e registro de usuários
- Histórico de conversas por usuário
- Upload de arquivos (.txt, .pdf, .docx, .pptx, .xlsx, .img) com OCR
- IA com contexto de conversa (usando Together AI)
- Tema escuro/claro
- Interface responsiva e acessível

## Tecnologias usadas

- Python (Flask)
- Together AI (LLaMA 3 70B)
- SQLite + SQLAlchemy
- HTML, CSS, JS
- Flask-Login
- OCR com Tesseract
- Deploy compatível com Heroku

## Como rodar localmente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Venti23/Chat-Bot-TEA.git
   ```

2. **Acesse a pasta do projeto**
   ```bash
   cd Chat-Bot-TEA
   ```

3. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   ```

4. **Ative o ambiente virtual**

   **No Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **No Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```

5. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

6. **Configuração do `.env`**
   - Renomeie o arquivo:
     ```bash
     mv .env.example .env
     ```
   - Abra o `.env` e edite com:
     - Sua **API Key**: [Obtenha aqui](https://api.together.ai/)
     - Sua **Secret Key**: gere executando:
       ```python
       import secrets
       print(secrets.token_hex(16))
       ```

7. **Execute o chatbot**
   ```bash
   python Serv.py
   ```

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato

**Vitor Oliveira Gomes**  
[GitHub](https://github.com/VitorOliveiraGomes) | [LinkedIn](https://www.linkedin.com/in/vitor-oliveira-gomes-610670317)

**Kaian Perez**  
[GitHub](https://github.com/kaiiiarchives) | [LinkedIn](https://www.linkedin.com/in/kaian-perez-7803792bb/)

