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
