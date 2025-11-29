import csv
import os

# ---------------------------------------
# 1. Função para criar o arquivo com cabeçalho (se não existir)
# ---------------------------------------
def criar_arquivo_csv(arquivo="notas.csv"):
    # Se o arquivo ainda não existe, cria com o cabeçalho
    if not os.path.exists(arquivo):
        with open(arquivo, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["Aluno", "Disciplina", "Nota"])  # Cabeçalho


# ---------------------------------------
# 2. Função para adicionar nota ao CSV
# ---------------------------------------
def adicionar_nota(nome, disciplina, nota, arquivo="notas.csv"):
    criar_arquivo_csv(arquivo)  # Garante que o arquivo exista

    # Converter nota para string, garantindo compatibilidade
    nota = str(nota)

    with open(arquivo, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([nome, disciplina, nota])

    print(f"Nota de {nome} registrada com sucesso!")


# ---------------------------------------
# 3. Função para carregar todas as notas
# ---------------------------------------
def carregar_notas(arquivo="notas.csv"):
    if not os.path.exists(arquivo):
        print("⚠ Arquivo não encontrado. Adicione notas primeiro.")
        return []

    notas = []

    with open(arquivo, mode="r", encoding="utf-8") as f:
        leitor = csv.reader(f)

        # Tenta pular o cabeçalho; evita erro se o arquivo estiver vazio
        try:
            next(leitor)
        except StopIteration:
            return []

        for linha in leitor:
            # Evita erros com linhas vazias ou incompletas
            if len(linha) == 3:
                notas.append(linha)

    return notas


# ---------------------------------------
# 4. Função para exibir notas de forma organizada
# ---------------------------------------
def exibir_notas(notas):
    if not notas:
        print("Nenhuma nota para exibir.")
        return

    print("\n📘 Lista de Notas Registradas:\n")
    print("Aluno | Disciplina | Nota")
    print("-" * 35)

    for nome, disciplina, nota in notas:
        print(f"{nome} | {disciplina} | {nota}")


# ---------------------------------------
# 5. EXEMPLO DE USO
# ---------------------------------------

# Adicionando algumas notas
adicionar_nota("Mariana", "Matemática", 9.0)
adicionar_nota("João", "História", 8.5)
adicionar_nota("Lucas", "Português", 7.8)

# Carregando as notas do arquivo
dados = carregar_notas()

# Exibindo as notas
exibir_notas(dados)
