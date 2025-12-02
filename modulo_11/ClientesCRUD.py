import sqlite3

# ------------------------------
# 1. Criar banco e tabela
# ------------------------------
def criar_tabela():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela criada com sucesso!")

# ------------------------------
# 2. Operações CRUD
# ------------------------------

def inserir_cliente(nome, email):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))

    conexao.commit()
    conexao.close()
    print(f"Cliente '{nome}' inserido com sucesso!")


def consultar_clientes():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    registros = cursor.fetchall()

    conexao.close()
    return registros


def atualizar_cliente(id_cliente, novo_nome, novo_email):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", 
                   (novo_nome, novo_email, id_cliente))

    conexao.commit()
    conexao.close()
    print("Cliente atualizado com sucesso!")


def deletar_cliente(id_cliente):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))

    conexao.commit()
    conexao.close()
    print("Cliente deletado com sucesso!")

# ------------------------------
# 3. Consulta filtrada (nome iniciando com A)
# ------------------------------

def consultar_clientes_com_a():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")
    resultado = cursor.fetchall()

    conexao.close()
    return resultado

# ------------------------------
# Programa de teste
# ------------------------------

if __name__ == "__main__":
    criar_tabela()

    print("\nInserindo clientes...")
    inserir_cliente("André", "andre@email.com")
    inserir_cliente("Ana", "ana@email.com")
    inserir_cliente("Bruno", "bruno@email.com")

    print("\nClientes cadastrados:")
    for c in consultar_clientes():
        print(c)

    print("\nAtualizando cliente de id 1...")
    atualizar_cliente(1, "André Emílio", "andre.emilio@email.com")

    print("\nClientes cujo nome começa com A:")
    for c in consultar_clientes_com_a():
        print(c)

    print("\nDeletando cliente de id 3...")
    deletar_cliente(3)

    print("\nLista final:")
    for c in consultar_clientes():
        print(c)
