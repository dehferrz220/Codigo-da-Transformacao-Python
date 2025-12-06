# app.py - Exemplo de API Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados para a API
db_registros = []

@app.route('/registrar', methods=['POST'])
def registrar_nfp():
    data = request.get_json()
    
    # Validações básicas (você expandiria isso)
    if 'cpf' not in data or 'valor' not in data:
        return jsonify({"erro": "Dados de CPF e Valor são obrigatórios."}), 400
        
    # Lógica de registro real/simulada aqui...
    registro = {
        "cpf": data['cpf'],
        "valor": data['valor'],
        "status": "Recebido"
    }
    db_registros.append(registro)
    
    return jsonify({"mensagem": "Registro recebido com sucesso.", "dados": registro}), 201

if __name__ == '__main__':
    app.run(debug=True)