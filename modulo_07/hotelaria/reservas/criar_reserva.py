from util.banco import reservas, quartos

def criar_reserva(nome_hospede, numero_quarto, dias):
    # Verifica se o quarto existe
    quarto = next((q for q in quartos if q["numero"] == numero_quarto), None)
    
    if not quarto:
        print("Quarto não encontrado.")
        return
    
    reserva = {
        "hospede": nome_hospede,
        "quarto": numero_quarto,
        "dias": dias,
        "valor_total": quarto["preco"] * dias
    }
    
    reservas.append(reserva)
    print(f"Reserva criada para {nome_hospede} no quarto {numero_quarto}.")
