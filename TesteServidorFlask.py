from flask import Flask, request, jsonify, render_template
from together import Together
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Permite que o front acesse a API

# Inicializa o cliente Together com a chave da API
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")  # Renderiza o front-end

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Mensagem vazia"}), 400

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[{"role": "user", "content": user_message}]
        )

        bot_message = response.choices[0].message.content
        return jsonify({"response": bot_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
