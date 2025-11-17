# ====================================================================
# ATIVIDADE 1: Saudação Personalizada
# Cria uma função que recebe um nome e imprime uma saudação personalizada.
# ====================================================================

def saudacao(nome):
  """
  Recebe um nome como parâmetro e exibe uma saudação personalizada.
  """
  print(f"Olá, {nome}! Seja muito bem-vindo(a)!")

# Exemplo de uso da Atividade 1
print("--- Atividade 1: Saudação ---")
saudacao("André Emílio")
print("-" * 30)


# ====================================================================
# ATIVIDADE 2: Cálculo de Média e Aprovação
# Cria uma função que calcula a média e determina se o aluno foi
# aprovado ou reprovado (média 7).
# ====================================================================

def calcular_media(notas):
  """
  Recebe uma lista de notas, calcula a média e determina se o aluno foi
  aprovado (média >= 7) ou reprovado.
  """
  if not notas:
    print("Erro: A lista de notas está vazia.")
    return "Lista Vazia"

  media = sum(notas) / len(notas)
  
  print(f"Média calculada: {media:.2f}")

  if media >= 7:
    print("Situação: APROVADO(A)!")
    return "Aprovado"
  else:
    print("Situação: REPROVADO(A)!")
    return "Reprovado"

# Exemplo de uso da Atividade 2
print("--- Atividade 2: Média e Aprovação ---")
notas_aprovado = [8.5, 7.0, 9.2, 6.8]
print("\nNotas (Aprovado):", notas_aprovado)
calcular_media(notas_aprovado)

notas_reprovado = [5.5, 6.0, 4.8, 7.0]
print("\nNotas (Reprovado):", notas_reprovado)
calcular_media(notas_reprovado)
print("-" * 30)


# ====================================================================
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


# ====================================================================
# DESAFIO EXTRA: Sistema de Login
# Cria um sistema simples de login com validação de usuário e senha
# usando um dicionário.
# ====================================================================

# Dicionário para armazenar dados de login: {usuario: senha}
DADOS_LOGIN = {
    "andre_emilio": "senhaforte123",
    "admin": "root",
    "visitante": "12345"
}

def validar_login(usuario, senha):
  """
  Valida se o usuário e senha fornecidos correspondem aos dados armazenados.
  Retorna True se o login for bem-sucedido, False caso contrário.
  """
  # Verifica se o usuário existe NO DICIONÁRIO E se a senha corresponde
  if usuario in DADOS_LOGIN and DADOS_LOGIN[usuario] == senha:
    return True
  else:
    return False

# Exemplos de uso do Desafio Extra
print("--- Desafio Extra: Sistema de Login ---")

# 1. Login com sucesso
if validar_login("andre_emilio", "senhaforte123"):
  print("✅ Login bem-sucedido para andre_emilio!")
else:
  print("❌ Falha no login para andre_emilio!")

# 2. Senha incorreta
if validar_login("admin", "senhaerrada"):
  print("✅ Login bem-sucedido para admin!")
else:
  print("❌ Falha no login para admin (Senha Incorreta)!")

# 3. Usuário inexistente
if validar_login("usuario_novo", "qualquersenha"):
  print("✅ Login bem-sucedido para usuario_novo!")
else:
  print("❌ Falha no login para usuario_novo (Usuário Inexistente)!")

print("-" * 30)