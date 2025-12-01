from hospedes.cadastro import cadastrar_hospede
from reservas.criar_reserva import criar_reserva
from relatorios.ocupacao import relatorio_ocupacao

def main():
    cadastrar_hospede("Ana Silva", 30, "RG12345")
    cadastrar_hospede("João Mendes", 45, "RG98765")

    criar_reserva("Ana Silva", 101, 3)
    criar_reserva("João Mendes", 201, 2)

    relatorio_ocupacao()

if __name__ == "__main__":
    main()
