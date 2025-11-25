
# ATIVIDADE 3: Maior e Menor Número em uma Lista
# Cria uma função que recebe uma lista de números e retorna o maior e o menor.
# ====================================================================

def maior_menor(lista_numeros):
  """
  Recebe uma lista de números e retorna o maior e o menor valores da lista
  como uma tupla (maior, menor).
  """
  if not lista_numeros:
    print("Erro: A lista de números está vazia.")
    return None, None
  
  # Uso das funções built-in 'max' e 'min' para eficiência
  maior = max(lista_numeros)
  menor = min(lista_numeros)
  
  print(f"Lista: {lista_numeros}")
  print(f"O maior valor é: {maior}")
  print(f"O menor valor é: {menor}")
  
  return maior, menor

# Exemplo de uso da Atividade 3
print("--- Atividade 3: Maior e Menor ---")
numeros = [15, 3, 22, 8, 45, 1, 10]
maior_valor, menor_valor = maior_menor(numeros)
print(f"Resultado retornado: ({maior_valor}, {menor_valor})")
print("-" * 30)


