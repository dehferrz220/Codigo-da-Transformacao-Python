"""
Sistema de Cadastro de Clientes usando POO
com persistência em arquivo JSON.

Atributos obrigatórios:
- nome
- idade
- cidade
- telefone
- email
- cpf

Métodos obrigatórios:
- inserir
- listar
- atualizar
- excluir

Arquivo principal: mod_08_cads_clientes.py
"""

import json
import os

# -------------------------------
# CONFIGURAÇÕES DE PERSISTÊNCIA
# -------------------------------

PASTA_DADOS = "dados"
ARQUIVO_DADOS = os.path.join(PASTA_DADOS, "clientes.json")


# -------------------------------
# CLASSE 1 — MODELAGEM DO CLIENTE
# -------------------------------

class Cliente:
    """Modela a entidade Cliente com seus atributos."""

    def __init__(self, nome, idade, cidade, telefone, email, cpf):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.cpf = cpf

    def to_dict(self):
        """Converte o objeto em dicionário para salvar no JSON."""
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade,
            "telefone": self.telefone,
            "email": self.email,
            "cpf": self.cpf
        }

    def __str__(self):
        """Representação textual para exibição."""
        return (f"Nome: {self.nome} | Idade: {self.idade} | Cidade: {self.cidade} | "
                f"Telefone: {self.telefone} | Email: {self.email} | CPF: {self.cpf}")

    def atualizar_dados(self, nome, idade, cidade, telefone, email, cpf):
        """Atualiza os dados do cliente."""
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        print(f"✔ Dados do cliente '{self.nome}' atualizados com sucesso.")


# ------------------------------------------
# CLASSE 2 — SISTEMA DE GERENCIAMENTO (POO)
# ------------------------------------------

class SistemaCadastro:
    """Gerencia toda a lógica do sistema e persistência em JSON."""

    def __init__(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.clientes = []
        self._carregar_dados()

    def _carregar_dados(self):
        """Carrega os dados do arquivo JSON ao iniciar o sistema."""
        if not os.path.exists(PASTA_DADOS):
            os.makedirs(PASTA_DADOS)

        try:
            with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                dados = json.load(f)

            self.clientes = [
                Cliente(
                    d.get("nome"),
                    d.get("idade"),
                    d.get("cidade"),
                    d.get("telefone", ""),
                    d.get("email", ""),
                    d.get("cpf", "")
                ) for d in dados
            ]

            print(f"✔ Dados carregados. Total de clientes: {len(self.clientes)}")

        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠ Nenhum arquivo encontrado. Criando um novo cadastro.")
            self.clientes = []

    def salvar_dados(self):
        """Salva as alterações no arquivo JSON."""
        dados = [cliente.to_dict() for cliente in self.clientes]

        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        print("💾 Dados salvos com sucesso.")

    def adicionar_cliente(self, nome, idade, cidade, telefone, email, cpf):
        novo = Cliente(nome, idade, cidade, telefone, email, cpf)
        self.clientes.append(novo)
        self.salvar_dados()
        print(f"🎉 Cliente '{nome}' cadastrado com sucesso!")

    def listar_clientes(self):
        print("\n--- LISTA DE CLIENTES ---")
        if not self.clientes:
            print("Nenhum cliente cadastrado.\n")
            return
        for i, cliente in enumerate(self.clientes, 1):
            print(f"[{i}] {cliente}")
        print("--------------------------\n")

    def atualizar_cliente(self, indice, nome, idade, cidade, telefone, email, cpf):
        try:
            cliente = self.clientes[indice - 1]
            cliente.atualizar_dados(nome, idade, cidade, telefone, email, cpf)
            self.salvar_dados()
        except IndexError:
            print("❌ ERRO: Cliente não encontrado.")

    def excluir_cliente(self, indice):
        try:
            removido = self.clientes.pop(indice - 1)
            self.salvar_dados()
            print(f"🗑 Cliente '{removido.nome}' removido com sucesso.")
        except IndexError:
            print("❌ ERRO: Índice inválido.")


# ------------------------------------------
# FUNÇÕES DE INTERFACE (ENTRADA DE DADOS)
# ------------------------------------------

def _obter_dados_cliente(modo="cadastro", dados_atuais=None):
    """Solicita dados ao usuário, reutilizando valores anteriores na atualização."""

    def entrada(campo, padrao=None, tipo=str):
        if modo == "atualizacao":
            texto = f"{campo} (atual: {padrao}) — ENTER mantém: "
        else:
            texto = f"{campo}: "

        valor = input(texto).strip()
        if modo == "atualizacao" and valor == "":
            return padrao
        if tipo == int:
            return int(valor)
        return valor

    nome = entrada("Nome", dados_atuais.get("nome") if dados_atuais else None)
    idade = entrada("Idade", dados_atuais.get("idade") if dados_atuais else None, tipo=int)
    cidade = entrada("Cidade", dados_atuais.get("cidade") if dados_atuais else None)
    telefone = entrada("Telefone", dados_atuais.get("telefone") if dados_atuais else None)
    email = entrada("Email", dados_atuais.get("email") if dados_atuais else None)
    cpf = entrada("CPF", dados_atuais.get("cpf") if dados_atuais else None)

    return nome, idade, cidade, telefone, email, cpf


# ------------------------------------------
# MENU PRINCIPAL — SISTEMA COMPLETO
# ------------------------------------------

def menu_principal():

    sistema = SistemaCadastro(ARQUIVO_DADOS)

    while True:
        print("""
=== MENU PRINCIPAL ===
0. Sair
1. Cadastrar novo cliente
2. Listar clientes
3. Atualizar cliente
4. Excluir cliente
""")

        opcao = input("Escolha uma opção: ").strip()

        # Sair
        if opcao == "0":
            print("Encerrando sistema... até mais!")
            break

        # Inserir
        elif opcao == "1":
            dados = _obter_dados_cliente()
            sistema.adicionar_cliente(*dados)

        # Listar
        elif opcao == "2":
            sistema.listar_clientes()

        # Atualizar
        elif opcao == "3":
            sistema.listar_clientes()
            try:
                idx = int(input("Digite o número do cliente: "))
                cliente = sistema.clientes[idx - 1]
                novos_dados = _obter_dados_cliente("atualizacao", cliente.to_dict())
                sistema.atualizar_cliente(idx, *novos_dados)
            except:
                print("❌ Entrada inválida.")

        # Excluir
        elif opcao == "4":
            sistema.listar_clientes()
            try:
                idx = int(input("Número do cliente para excluir: "))
                sistema.excluir_cliente(idx)
            except:
                print("❌ Entrada inválida.")

        else:
            print("Opção inválida. Tente novamente.")


# ---------------------------
# EXECUTAR O SISTEMA
# ---------------------------

if __name__ == "__main__":
    menu_principal()
