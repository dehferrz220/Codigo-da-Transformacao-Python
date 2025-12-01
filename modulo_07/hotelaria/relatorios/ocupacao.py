from util.banco import reservas

def relatorio_ocupacao():
    if not reservas:
        print("Nenhuma reserva encontrada.")
        return
    
    print("\n--- Relatório de Ocupação ---")
    for r in reservas:
        print(f"Hóspede: {r['hospede']} | Quarto: {r['quarto']} | Dias: {r['dias']}")
