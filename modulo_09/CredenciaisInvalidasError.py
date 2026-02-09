def login():
    usuario_correto = "admin"
    senha_correta = "1234"
    tentativas = 3

    while tentativas > 0:
        try:
            # Pede a entrada do usuário DENTRO do bloco try
            usuario = input("Usuário: ")
            senha = input("Senha: ")

            # Verifica as credenciais
            if usuario == usuario_correto and senha == senha_correta:
                print("Login bem-sucedido! Bem-vindo.")
                return True
            else:
                tentativas -= 1
                print(f"Credenciais inválidas. Tentativas restantes: {tentativas}")

        except Exception as e:
            # Captura qualquer erro inesperado (Exception)
            print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
            # Não decrementamos 'tentativas' aqui para não punir o usuário por um erro do sistema.

    print("Acesso bloqueado! Muitas tentativas incorretas.")
    return False


login()
