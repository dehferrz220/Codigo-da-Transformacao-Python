# test_api.py
import pytest
import json

# Fixture 'app' e 'client' são fornecidas pelo pytest-flask
# Supondo que você criou um arquivo conftest.py para configurar o app

def test_registrar_sucesso(client):
    """Testa se a rota /registrar aceita um payload válido."""
    response = client.post(
        '/registrar', 
        data=json.dumps({'cpf': '11122233344', 'valor': 150.00}),
        content_type='application/json'
    )
    assert response.status_code == 201
    assert b'Registro recebido com sucesso' in response.data

def test_registrar_erro_dados_ausentes(client):
    """Testa se a rota /registrar retorna erro com dados ausentes."""
    response = client.post(
        '/registrar', 
        data=json.dumps({'cpf': '11122233344'}), # Falta o 'valor'
        content_type='application/json'
    )
    assert response.status_code == 400
    assert b'Dados de CPF e Valor s' in response.data