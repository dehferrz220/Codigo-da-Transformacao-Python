print("\n" + "="*40)
print("--- Programa: Classificador de Idade ---")

try:
    idade = int(input("Digite sua idade: "))
    
    print("-" * 30)
    
    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Classificação: Criança.")
    elif idade <= 17:
        print("Classificação: Adolescente.")
    elif idade <= 35:
        print("Classificação: Adulto.")
    elif idade <= 339:
        print("Classificação: Idoso.")

except ValueError:
    print("\nERRO: Entrada inválida. Por favor, digite um número inteiro para a idade.")

