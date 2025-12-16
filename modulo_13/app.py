from flask import Flask, request, jsonify
import sqlite3
import os

# -------------------------
# Configurações iniciais
# -------------------------
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'database.db')


# -------------------------
# Funções do banco de dados
# -------------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# -------------------------
# Rota GET /saudacao
# -------------------------
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({
        "mensagem": "Olá! API Flask funcionando corretamente 🚀"
    }), 200


# -------------------------
# Rota POST /cadastrar
# -------------------------
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    if not request.is_json:
        return jsonify({
            "erro": "A requisição deve estar no formato JSON."
        }), 400

    dados = request.get_json()

    nome = dados.get('nome')
    email = dados.get('email')

    if not nome or not email:
        return jsonify({
            "erro": "Os campos 'nome' e 'email' são obrigatórios."
        }), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
            (nome, email)
        )

        conn.commit()
        conn.close()

        return jsonify({
            "mensagem": "Usuário cadastrado com sucesso!",
            "usuario": {
                "nome": nome,
                "email": email
            }
        }), 201

    except Exception as e:
        return jsonify({
            "erro": "Erro ao cadastrar usuário.",
            "detalhes": str(e)
        }), 500


# -------------------------
# Inicialização da aplicação
# -------------------------
if __name__ == '__main__':
    init_db()

    # debug=True ajuda no ambiente de desenvolvimento
    # host='0.0.0.0' evita problemas em alguns ambientes
    app.run(
        debug=True,
        host='127.0.0.1',
        port=5000
    )
