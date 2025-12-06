import unittest
from sistema_nfp import Hospede, GerenciadorNFP

class TestHospede(unittest.TestCase):
    """Testa a classe Hospede e validação de CPF."""

    def test_cpf_limpo(self):
        """Verifica se o CPF é limpo e armazenado corretamente."""
        hospede = Hospede("Teste", "111.222.333-44", "a@a.com")
        self.assertEqual(hospede.cpf, "11122233344")

    def test_cpf_com_onze_digitos(self):
        """Verifica se um CPF válido é aceito."""
        hospede = Hospede("Teste", "12345678901", "a@a.com")
        self.assertEqual(len(hospede.cpf), 11)

    def test_cpf_invalido_curto(self):
        """Verifica se um CPF com menos de 11 dígitos levanta ValueError."""
        with self.assertRaises(ValueError):
            Hospede("Teste", "123", "a@a.com")

    def test_cpf_tipo_incorreto(self):
        """Verifica se uma entrada não-string para CPF levanta TypeError."""
        with self.assertRaises(TypeError):
            Hospede("Teste", 12345678901, "a@a.com")

class TestGerenciadorNFP(unittest.TestCase):
    """Testa a classe GerenciadorNFP e o registro de dados."""
    
    # Função que será executada antes de cada método de teste
    def setUp(self):
        self.gerenciador = GerenciadorNFP()
        self.hospede_valido = Hospede("Teste NFP", "00000000000", "nfp@teste.com")

    def test_registro_estadia(self):
        """Verifica se um registro é adicionado corretamente."""
        self.gerenciador.registrar_estadia(self.hospede_valido, 100.00)
        self.assertEqual(len(self.gerenciador.registros), 1)
        self.assertEqual(self.gerenciador.registros[0]['valor_estadia'], 100.00)
        
    def test_registro_tipo_invalido(self):
        """Verifica se registrar_estadia rejeita entradas não-Hospede."""
        with self.assertRaises(TypeError):
            self.gerenciador.registrar_estadia("nao-hospede", 50.00)
            
    # Para testar planilhamento, você precisaria criar um arquivo temporário
    # para evitar sobrescrever dados, mas isso adiciona complexidade. 
    # Focaremos na lógica interna por enquanto.

if __name__ == '__main__':
    unittest.main()