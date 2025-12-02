# ---------------------------------------------
# Arquivo: clima.py
# Funções para consumir a API do OpenWeatherMap
# ---------------------------------------------

import requests

API_KEY = "SUA_API_KEY_AQUI"  # Coloque sua chave aqui
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def obter_clima(cidade):
    """
    Faz a requisição para a API do OpenWeatherMap
    e retorna os dados em formato JSON.
    """
    try:
        params = {
            "q": cidade,
            "appid": API_KEY,
            "lang": "pt_br",
            "units": "metric"
        }

        resposta = requests.get(BASE_URL, params=params)
        resposta.raise_for_status()
        return resposta.json()

    except requests.exceptions.RequestException as erro:
        print("❌ Erro ao conectar à API:", erro)
        return None


def exibir_informacoes(dados):
    """
    Exibe temperatura e condições climáticas.
    """
    if dados is None:
        print("Nenhuma informação disponível.")
        return

    cidade = dados["name"]
    temperatura = dados["main"]["temp"]
    condicao = dados["weather"][0]["description"]

    print("\n======= PREVISÃO DO TEMPO =======")
    print(f"📍 Cidade: {cidade}")
    print(f"🌡️ Temperatura: {temperatura}°C")
    print(f"⛅ Condições: {condicao.capitalize()}")
    print("=================================\n")
