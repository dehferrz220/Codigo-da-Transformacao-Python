## ATIVIDADE 2: Exceção Personalizada SaldoInsuficienteError

# 2. Crie uma exceção personalizada SaldoInsuficienteError
class SaldoInsuficienteError(Exception):
    """
    Exceção personalizada para simular casos de saldo insuficiente em contas bancárias.
    """
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        super().__init__(f"Tentativa de saque de R${valor_saque:.2f} falhou. Saldo atual: R${saldo_atual:.2f}")

class ContaBancaria:
    """
    Simulação de conta bancária para demonstrar o uso da exceção personalizada.
    """
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Conta de {self.titular} criada com saldo inicial de R${self.saldo:.2f}")

    # 3. Adiciona validação para garantir que o saque seja um número positivo
    def sacar(self, valor):
        """
        Realiza um saque e levanta a exceção SaldoInsuficienteError se necessário.
        """
        if valor <= 0:
            # Validação (Atividade 3)
            print("Erro de Saque: O valor do saque deve ser positivo.")
            return

        try:
            if valor > self.saldo:
                # Levanta a exceção personalizada
                raise SaldoInsuficienteError(self.saldo, valor)
            
            # Saque realizado com sucesso
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

        except SaldoInsuficienteError as e:
            # Captura e trata a exceção personalizada
            print(f"\nERRO BANCÁRIO: {e}")
        except Exception as e:
            print(f"\nOCORREU UM ERRO INESPERADO: {e}")

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor <= 0:
            # Validação (Atividade 3)
            print("Erro de Depósito: O valor do depósito deve ser positivo.")
            return
        
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

# --- Teste da Conta Bancária e Exceção Personalizada ---

print("\n--- TESTE CONTA BANCÁRIA ---")
minha_conta = ContaBancaria("João Silva", 150.00)
minha_conta.consultar_saldo()

# 1. Tentativa de saque bem-sucedido
minha_conta.sacar(50.00)
minha_conta.consultar_saldo()

# 2. Tentativa de saque que dispara a exceção SaldoInsuficienteError
minha_conta.sacar(150.00) # Vai disparar a exceção personalizada

# 3. Teste de validação (saque de valor não positivo)
minha_conta.sacar(-10.00) 
minha_conta.depositar(0.00)