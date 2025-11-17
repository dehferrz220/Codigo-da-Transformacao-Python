# 🧮 Sistema de Cálculo de Notas — Versão Aprimorada
# Autor: André Emílio Ferraz (LIO Studios)
# Slogan: "Cada nota é uma história"

from datetime import datetime

# Função para calcular a média
def calcula_media(notas):
    return sum(notas) / len(notas)

# Função para verificar a situação do aluno
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado ✅"
    elif 5 <= media < 7:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"

# Função para exibir e salvar o resultado
def exibir_resultado(nome, notas):
    media = calcula_media(notas)
    situacao = verificar_situacao(media)

    print("\n📊 Resultado Final")
    print("=" * 30)
    print(f"Aluno: {nome}")
    print(f"Notas: {', '.join(map(str, notas))}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("=" * 30)

    # Salvando os dados no arquivo
    with open("resultado.txt", "a", encoding="utf-8") as arquivo:
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        arquivo.write(f"\n[{data}] {nome} - Notas: {notas} - Média: {media:.2f} - {situacao}")

# Programa principal
def main():
    print("🎓 Sistema de Cálculo de Notas — LIO Studios")
    print("Cada nota é uma história.\n")

    nome = input("Digite o nome do aluno: ")

    notas = []
    while True:
        nota = input("Digite uma nota (ou 'fim' para encerrar): ")
        if nota.lower() == "fim":
            break
        try:
            notas.append(float(nota))
        except ValueError:
            print("⚠️ Por favor, digite um número válido.")

    if notas:
        exibir_resultado(nome, notas)
    else:
        print("Nenhuma nota foi informada. Encerrando o programa.")

# Executar o programa
if __name__ == "__main__":
    main()
