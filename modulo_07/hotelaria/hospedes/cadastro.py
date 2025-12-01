from util.banco import hospedes

def cadastrar_hospede(nome, idade, documento):
    hospede = {
        "nome": nome,
        "idade": idade,
        "documento": documento
    }
    hospedes.append(hospede)
    print(f"Hóspede {nome} cadastrado com sucesso.")
