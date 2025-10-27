# 🧮 Atividade 1 — Dados de um aluno em um dicionário

aluno = {
    "nome": "Ana Clara",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5]
}

print("📚 Dados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")


# 🛒 Atividade 2 — Lista de Compras

lista_compras = []

while True:
    print("\n--- Lista de Compras ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.append(item)
        print(f"✅ {item} foi adicionado à lista.")
        
    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"❌ {item} foi removido da lista.")
        else:
            print("⚠️ Item não encontrado.")
            
    elif opcao == "3":
        print("\n🛍️ Sua lista de compras:")
        for item in lista_compras:
            print(f"- {item}")
            
    elif opcao == "4":
        print("Encerrando o programa...")
        break
        
    else:
        print("Opção inválida! Tente novamente.")


# 🔢 Atividade 3 — Números pares e ímpares

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("🔹 Números pares:", pares)
print("🔸 Números ímpares:", impares)


# 💡 Desafio Extra — Sistema de Agenda de Contatos

agenda = {}

while True:
    print("\n--- Agenda de Contatos ---")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Ver todos os contatos")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print(f"✅ Contato {nome} adicionado com sucesso!")
        
    elif opcao == "2":
        nome = input("Nome do contato a remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"❌ Contato {nome} removido.")
        else:
            print("⚠️ Contato não encontrado.")
            
    elif opcao == "3":
        nome = input("Nome do contato a buscar: ")
        if nome in agenda:
            print(f"📞 {nome}: {agenda[nome]}")
        else:
            print("⚠️ Contato não encontrado.")
            
    elif opcao == "4":
        print("\n📖 Contatos na agenda:")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
            
    elif opcao == "5":
        print("Saindo da agenda...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")
