import csv

# Criar e salvar notas
with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Aluno", "Nota"])
    escritor.writerow(["André", 9.5])
    escritor.writerow(["Laís", 8.7])
    escritor.writerow(["Henrique", 7.9])

# Ler e exibir notas
with open("notas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
