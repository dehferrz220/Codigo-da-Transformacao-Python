# 1. Crie uma classe Carro com atributos como marca, modelo e método exibir_info().
class Carro:
    """
    Representa um veículo genérico com marca e modelo.
    """
    # 3. Use métodos especiais como __init__ para personalizar a inicialização
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"Um novo Carro ({self.marca} {self.modelo}) foi criado.")

    def exibir_info(self):
        """Exibe as informações básicas do carro."""
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
    # 3. Use métodos especiais como __str__ para personalizar a exibição de objetos.
    def __str__(self):
        """Retorna uma representação em string do objeto Carro."""
        return f"Carro: {self.marca} {self.modelo}"

# 2. Implemente herança: Crie uma classe CarroEletrico que herda de Carro e adiciona autonomia_bateria.
class CarroEletrico(Carro):
    """
    Representa um carro elétrico, herdando de Carro e adicionando autonomia de bateria.
    """
    def __init__(self, marca, modelo, autonomia_bateria):
        # Chama o construtor da classe pai (Carro)
        super().__init__(marca, modelo) 
        self.autonomia_bateria = autonomia_bateria # Atributo exclusivo
        print(f"Um Carro Elétrico (Autonomia: {self.autonomia_bateria} km) foi criado.")

    # Sobrescreve o método exibir_info para incluir a autonomia
    def exibir_info(self):
        """Exibe as informações do carro elétrico, incluindo a autonomia."""
        info_pai = super().exibir_info() # Pega as informações básicas do Carro
        return f"{info_pai}, Autonomia da Bateria: {self.autonomia_bateria} km"
    
    # 3. Use métodos especiais como __str__ (sobrescrevendo o da classe pai)
    def __str__(self):
        """Retorna uma representação em string do objeto CarroEletrico."""
        return f"Carro Elétrico: {self.marca} {self.modelo} (Autonomia: {self.autonomia_bateria} km)"

# --- Exemplos de Uso das Classes Principais ---

print("\n--- TESTE CLASSES CARRO e CARROELETRICO ---")

# Criação de objetos
meu_carro = Carro("Toyota", "Corolla")
meu_eletrico = CarroEletrico("Tesla", "Model 3", 450)

print("-" * 20)

# 1. e 2. Teste do método exibir_info()
print(f"Info Carro: {meu_carro.exibir_info()}")
print(f"Info Carro Elétrico: {meu_eletrico.exibir_info()}")

print("-" * 20)

# 3. Teste do método especial __str__ (chamado pela função print())
print(f"Representação String Carro: {meu_carro}")
print(f"Representação String Carro Elétrico: {meu_eletrico}")