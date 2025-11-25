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
