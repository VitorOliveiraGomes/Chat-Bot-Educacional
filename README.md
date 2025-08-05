# Chatbot Educacional para TEA

Este é um **chatbot educacional desenvolvido com Flask**, voltado para auxiliar pessoas com **Transtorno do Espectro Autista (TEA)**. Ele utiliza o modelo **LLaMA 3.3 70B**, via [Together API](https://www.together.ai/), para gerar explicações claras e passo a passo com base nos conteúdos fornecidos.

---

## Objetivo

Fornecer uma ferramenta digital simples, acessível e empática para apoiar o aprendizado de pessoas com TEA, por meio de uma interface web intuitiva e responsiva.

---

## Funcionalidades

- Interface web responsiva com suporte a tema claro/escuro
- Sistema de **login e registro de usuários**
- Histórico de conversas por usuário
- Suporte a **envio de arquivos** (.txt, .pdf, .docx, .xlsx, .pptx, .jpg, .png)
- IA personalizada com prompt adaptado para pessoas com TEA
- Armazenamento das mensagens com timestamp no banco de dados
- Processamento e leitura de arquivos de texto, planilhas, apresentações, imagens e PDFs

---

## Tecnologias Utilizadas

- Python 3
- Flask + Flask-CORS
- Flask-Login + Flask-SQLAlchemy
- Together API (modelo LLaMA 3.3 70B)
- HTML, CSS, JavaScript puro
- Gunicorn (produção)
- dotenv (variáveis de ambiente)
- PyPDF2, python-docx, pandas, python-pptx, pytesseract (processamento de arquivos)

---
<img width="1902" height="919" alt="image" src="https://github.com/user-attachments/assets/c1e4fed6-c002-4409-a3e6-3d97a1dce092" />
<img width="1888" height="904" alt="image" src="https://github.com/user-attachments/assets/03d109de-a6b0-48bf-9f74-7122aadc3457" />
<img width="1893" height="916" alt="image" src="https://github.com/user-attachments/assets/052f9ce9-aa56-4d34-80c9-01bd89a3860f" />


## Estrutura do Projeto

```bash
/
├── Serv.py                # Backend principal com rotas Flask
├── models.py              # Modelos de banco (User, Message, Conversation)
├── prompt.txt             # Prompt base para IA voltado ao público TEA
├── requirements.txt       # Dependências do Python
├── Templates/
│   ├── index.html         # Interface principal do chatbot
│   ├── login.html         # Página de login
│   └── register.html      # Página de registro
├── static/
│   └── css/style.css      # Estilos da interface
└── instance/db.sqlite3    # Banco de dados SQLite (criado automaticamente)

---

Como Executar Localmente
    ```bash
    # 1. Clone o repositório
    git clone https://github.com/VitorOliveiraGomes/Chat-Bot-Educacional.git
    cd Chat-Bot-Educacional

    # 2. Crie um ambiente virtual
    python -m venv venv
    # Ative o ambiente (use o comando de acordo com seu sistema):
    source venv/bin/activate        # Linux/macOS
    venv\Scripts\activate           # Windows

    # 3. Instale as dependências
    pip install -r requirements.txt

    # 4. Altero o arquivo .env.example para .env e adicione a chave da API do Together
    
    # 5. Execute o servidor
    python Serv.py
---
Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Contato

Vitor Oliveira  
GitHub: [https://github.com/VitorOliveiraGomes](https://github.com/VitorOliveiraGomes)
Linkedin: [www.linkedin.com/in/vitor-oliveira-gomes-610670317](www.linkedin.com/in/vitor-oliveira-gomes-610670317)
Kaian Perez
GitHub: [https://github.com/kaiiiarchives](https://github.com/kaiiiarchives)
Linkedin: [https://www.linkedin.com/in/kaian-perez-7803792bb/](https://www.linkedin.com/in/kaian-perez-7803792bb/)
