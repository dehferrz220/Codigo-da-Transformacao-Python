def calculadora():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao == "+":
            print("Resultado:", n1 + n2)
        elif operacao == "-":
            print("Resultado:", n1 - n2)
        elif operacao == "*":
            print("Resultado:", n1 * n2)
        elif operacao == "/":
            try:
                print("Resultado:", n1 / n2)
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero!")
        else:
            print("Operação inválida.")

    except ValueError:
        print("Erro: Digite apenas números válidos.")


calculadora()
