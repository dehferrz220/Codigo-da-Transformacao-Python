import json

clientes = {
    "cliente1": {"nome": "Ana", "idade": 25},
    "cliente2": {"nome": "Carlos", "idade": 32}
}

# Salvar JSON
with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

# Carregar JSON
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("Clientes carregados do JSON:")
print(dados)
