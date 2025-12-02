# ---------------------------------------------
# Arquivo: main_tmdb.py
# Programa para buscar filmes usando o TMDB
# ---------------------------------------------

from tmdb import buscar_filme, exibir_filme

def main():
    print("=== Busca de Filmes (TMDB) ===")
    nome = input("Digite o nome do filme: ")
    filme = buscar_filme(nome)
    exibir_filme(filme)


if __name__ == "__main__":
    main()
