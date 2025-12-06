import pandas as pd
from datetime import datetime

# ===============================================
# 1. Classe para o CRM/Hospede
# ===============================================
class Hospede:
    """Representa um hóspede e seus dados para NFP."""
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = self._limpar_cpf(cpf)
        self.email = email
        self.pontuacao_crm = 0  # Exemplo de dado de CRM
        
    def _limpar_cpf(self, cpf):
        """Remove caracteres não numéricos do CPF."""
        if not isinstance(cpf, str):
            raise TypeError("CPF deve ser uma string.")
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        if len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter 11 dígitos.")
        return cpf_limpo

# ===============================================
# 2. Classe para Contabilização (Fictícia)
# ===============================================
class GerenciadorNFP:
    """Gerencia registros e dados planilhados."""
    def __init__(self):
        # Lista de dicionários para armazenar os dados de cada estadia/registro
        self.registros = []

    def registrar_estadia(self, hospede, valor_estadia):
        """Simula o registro de uma estadia e potencial NFP."""
        if not isinstance(hospede, Hospede):
            raise TypeError("O objeto deve ser uma instância de Hospede.")
            
        # Simulação de dados coletados/calculados
        registro = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'cpf': hospede.cpf,
            'nome_hospede': hospede.nome,
            'valor_estadia': valor_estadia,
            'valor_nfp_simulado': valor_estadia * 0.05, # Simulação de 5% de crédito
            'status_nfp': 'Pendente Contabilização',
            'pontuacao_crm_atual': hospede.pontuacao_crm
        }
        self.registros.append(registro)
        print(f"Registro de estadia para CPF {hospede.cpf} concluído.")
        
    def planilhar_dados(self, nome_arquivo="relatorio_nfp.xlsx"):
        """Converte os registros em um DataFrame Pandas e salva em Excel."""
        if not self.registros:
            print("Nenhum registro para planilhar.")
            return

        df = pd.DataFrame(self.registros)
        
        # Exemplo de manipulação de dados
        df['data'] = pd.to_datetime(df['timestamp']).dt.date
        
        # Colunas na ordem desejada
        colunas = ['data', 'cpf', 'nome_hospede', 'valor_estadia', 'valor_nfp_simulado', 'status_nfp', 'pontuacao_crm_atual']
        df = df[colunas]
        
        # Salva o DataFrame em um arquivo Excel (requer a biblioteca openpyxl instalada)
        df.to_excel(nome_arquivo, index=False)
        print(f"\nDados exportados com sucesso para '{nome_arquivo}'")
        
# Exemplo de Uso
if __name__ == '__main__':
    # Cria o gerenciador
    gerenciador = GerenciadorNFP()
    
    # Cria e registra hóspedes
    hospede1 = Hospede("Joao Silva", "123.456.789-00", "joao@exemplo.com")
    hospede2 = Hospede("Maria Souza", "98765432101", "maria@exemplo.com")
    
    gerenciador.registrar_estadia(hospede1, 550.00)
    gerenciador.registrar_estadia(hospede2, 1200.50)
    
    # Gera a planilha
    gerenciador.planilhar_dados()