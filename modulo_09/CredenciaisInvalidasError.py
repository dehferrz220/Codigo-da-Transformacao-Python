def login():
    usuario_correto = "admin"
    senha_correta = "1234"
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login bem-sucedido! Bem-vindo.")
            return True
        else:
            tentativas -= 1
            print(f"Credenciais inválidas. Tentativas restantes: {tentativas}")

    print("Acesso bloqueado! Muitas tentativas incorretas.")
    return False


login()
