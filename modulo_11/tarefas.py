import sqlite3

# ------------------------------------
# Criar banco e tabela de tarefas
# ------------------------------------
def criar_tabela_tarefas():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'Pendente'
        );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela de tarefas criada com sucesso!")


# ------------------------------------
# Inserir tarefa
# ------------------------------------
def adicionar_tarefa(titulo, descricao=None):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)",
                   (titulo, descricao))

    conexao.commit()
    conexao.close()
    print(f"Tarefa '{titulo}' adicionada com sucesso!")


# ------------------------------------
# Listar todas as tarefas
# ------------------------------------
def listar_tarefas():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    conexao.close()
    return tarefas


# ------------------------------------
# Atualizar tarefa (título e descrição)
# ------------------------------------
def atualizar_tarefa(id_tarefa, novo_titulo, nova_descricao):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas 
        SET titulo = ?, descricao = ?
        WHERE id = ?
    """, (novo_titulo, nova_descricao, id_tarefa))

    conexao.commit()
    conexao.close()
    print("Tarefa atualizada com sucesso!")


# ------------------------------------
# Marcar como concluída
# ------------------------------------
def concluir_tarefa(id_tarefa):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("UPDATE tarefas SET status = 'Concluída' WHERE id = ?", (id_tarefa,))

    conexao.commit()
    conexao.close()
    print("Tarefa marcada como concluída!")


# ------------------------------------
# Excluir tarefa
# ------------------------------------
def excluir_tarefa(id_tarefa):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))

    conexao.commit()
    conexao.close()
    print("Tarefa excluída com sucesso!")


# ------------------------------------
# Programa de demonstração
# ------------------------------------
if __name__ == "__main__":
    criar_tabela_tarefas()

    print("\nAdicionando tarefas...")
    adicionar_tarefa("Estudar Python", "Praticar SQLite")
    adicionar_tarefa("Criar Projeto", "Desafio do curso de Hotelaria")
    adicionar_tarefa("Gravar vídeo", "Explicar o sistema de tarefas")

    print("\nTarefas cadastradas:")
    for t in listar_tarefas():
        print(t)

    print("\nConcluindo tarefa 2...")
    concluir_tarefa(2)

    print("\nAtualizando tarefa 1...")
    atualizar_tarefa(1, "Estudar Python Avançado", "Criar CRUD completo")

    print("\nTarefas após atualizações:")
    for t in listar_tarefas():
        print(t)

    print("\nExcluindo tarefa 3...")
    excluir_tarefa(3)

    print("\nLista final de tarefas:")
    for t in listar_tarefas():
        print(t)
