# ---------------------------------------------
# Arquivo: main_clima.py
# Executa o programa de previsão do tempo
# ---------------------------------------------

from clima import obter_clima, exibir_informacoes

def main():
    print("=== Consulta de Clima ===")
    cidade = input("Digite o nome da cidade: ")
    dados = obter_clima(cidade)
    exibir_informacoes(dados)


if __name__ == "__main__":
    main()
