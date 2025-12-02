# ---------------------------------------------
# Arquivo: tmdb.py
# Consumo da API do TMDB (filmes)
# ---------------------------------------------

import requests

TMDB_KEY = "SUA_API_KEY_TMDB_AQUI"
TMDB_URL = "https://api.themoviedb.org/3/search/movie"


def buscar_filme(nome_filme):
    """
    Faz uma requisição ao TMDB e retorna o primeiro resultado encontrado.
    """
    try:
        params = {
            "api_key": TMDB_KEY,
            "query": nome_filme,
            "language": "pt-BR"
        }

        resposta = requests.get(TMDB_URL, params=params)
        resposta.raise_for_status()

        dados = resposta.json()

        if dados["results"]:
            return dados["results"][0]
        else:
            print("Nenhum filme encontrado.")
            return None

    except requests.exceptions.RequestException as erro:
        print("❌ Erro ao acessar o TMDB:", erro)
        return None


def exibir_filme(filme):
    """
    Exibe informações sobre um filme buscado no TMDB.
    """
    if filme is None:
        return

    print("\n======= FILME ENCONTRADO =======")
    print(f"🎬 Título: {filme['title']}")
    print(f"📅 Lançamento: {filme['release_date']}")
    print(f"⭐ Nota: {filme['vote_average']} / 10")
    print(f"📖 Sinopse: {filme['overview']}")
    print("=================================\n")
