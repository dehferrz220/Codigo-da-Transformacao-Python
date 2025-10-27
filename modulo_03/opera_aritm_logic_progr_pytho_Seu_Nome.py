'''
OPERADORES ARITMÉTICOS
Este programa demonstra as 5 operações básicas com 2 números.
Peça ao usuario para digitar 2 números inteiros e mostre:
- A soma
- A diferença (subtração)
- A multiplicação
- A divisão
- O módulo (resto da divisão)

'''


# 1. PEDIR OS NÚMEROS AO UTILIZADOR (USUÁRIO)

# A função 'input()' pede algo e guarda como texto.
# 'int()' converte o texto que o utilizador digitou num número inteiro.
try:
    numero1 = int(input("Digite o primeiro número (Ex: 10): "))
    numero2 = int(input("Digite o segundo número (Ex: 5): "))
except ValueError:
    print("\nERRO: Por favor, digite apenas números inteiros.")
    # Saímos do programa se houver um erro, para evitar problemas nas contas.
    exit() 

print("\n--- Resultados das Operações ---")

# 2. REALIZAR E MOSTRAR AS OPERAÇÕES

# SOMA (+)
soma = numero1 + numero2
print(f"1. SOMA: {numero1} + {numero2} = {soma}")

# DIFERENÇA ou SUBTRAÇÃO (-)
diferenca = numero1 - numero2
print(f"2. SUBTRAÇÃO: {numero1} - {numero2} = {diferenca}")

# MULTIPLICAÇÃO (*)
multiplicacao = numero1 * numero2
print(f"3. MULTIPLICAÇÃO: {numero1} * {numero2} = {multiplicacao}")

# DIVISÃO (/) - Usa-se '//' para divisão de inteiros (sem casas decimais)
# Vamos usar '/' que é a divisão comum (flutuante)
divisao = numero1 / numero2
print(f"4. DIVISÃO: {numero1} / {numero2} = {divisao}")

# MÓDULO ou RESTO DA DIVISÃO (%)
# O módulo dá o resto de uma divisão. Ex: 10 % 3 = 1
resto_divisao = numero1 % numero2
print(f"5. MÓDULO (Resto): {numero1} % {numero2} = {resto_divisao}")

print("\n---------------------------------")