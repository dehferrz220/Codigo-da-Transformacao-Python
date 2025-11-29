import json

def salvar_clientes_json():
    clientes = {
        "001": {"nome": "Lucas", "idade": 18, "status": "Ativa"},
        "002": {"nome": "Ana", "idade": 17, "status": "Ativo"},
        "003": {"nome": "André", "idade": 17, "status": "Administrador"}
    }

    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

def carregar_clientes_json():
    with open("clientes.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    print("\n🧾 CLIENTES CADASTRADOS (JSON):")
    for id, info in dados.items():
        print(f"- ID {id}: {info['nome']} ({info['idade']} anos) — {info['status']}")

salvar_clientes_json()
carregar_clientes_json()
