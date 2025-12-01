# Arquivo: jogo_adivinhacao.py

import random
import math # Importado conforme solicitado, mas não essencial para a lógica básica

def jogo_adivinhacao():
    # Gera um número aleatório inteiro entre 1 e 100
    numero_secreto = random.randint(1, 100) 
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        try:
            chute = int(input("Digite seu chute: "))
            tentativas += 1
            
            if chute < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            elif chute > numero_secreto:
                print("Muito alto! Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Executa a função do jogo
jogo_adivinhacao()