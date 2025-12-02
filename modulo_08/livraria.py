class Livro:
    """
    Representa um livro com título, autor e status de empréstimo.
    """
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True # O livro começa disponível
    
    def __str__(self):
        """Retorna a representação em string do Livro."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} ({status})"

class Biblioteca:
    """
    Gerencia uma coleção de Livros e os empréstimos.
    """
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = [] # Lista de objetos Livro
    
    def adicionar_livro(self, livro):
        """Adiciona um objeto Livro ao catálogo da biblioteca."""
        self.catalogo.append(livro)
        print(f"'{livro.titulo}' adicionado à biblioteca {self.nome}.")

    def emprestar_livro(self, titulo):
        """Tenta emprestar um livro pelo título."""
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"✅ Livro '{titulo}' emprestado com sucesso.")
                    return
                else:
                    print(f"❌ Livro '{titulo}' já está emprestado.")
                    return
        print(f"❌ Livro '{titulo}' não encontrado no catálogo.")

    def devolver_livro(self, titulo):
        """Tenta devolver um livro pelo título."""
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"✅ Livro '{titulo}' devolvido com sucesso.")
                    return
                else:
                    print(f"❌ Livro '{titulo}' já está disponível (não estava emprestado).")
                    return
        print(f"❌ Livro '{titulo}' não encontrado no catálogo.")

    def listar_catalogo(self):
        """Exibe todos os livros no catálogo e seu status."""
        print(f"\n--- Catálogo da Biblioteca {self.nome} ---")
        if not self.catalogo:
            print("O catálogo está vazio.")
            return

        for livro in self.catalogo:
            print(f"- {livro}")
        print("---------------------------------------")


# --- Exemplos de Uso do Desafio Extra ---

print("\n\n--- DESAFIO EXTRA: BIBLIOTECA ---")

# Inicialização
biblioteca_municipal = Biblioteca("Municipal Central")

# Criação e adição de livros
l1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
l2 = Livro("1984", "George Orwell")
l3 = Livro("Dom Casmurro", "Machado de Assis")

biblioteca_municipal.adicionar_livro(l1)
biblioteca_municipal.adicionar_livro(l2)
biblioteca_municipal.adicionar_livro(l3)

biblioteca_municipal.listar_catalogo()

# Teste de empréstimo
biblioteca_municipal.emprestar_livro("1984") # Sucesso
biblioteca_municipal.emprestar_livro("1984") # Falha (já emprestado)
biblioteca_municipal.emprestar_livro("O Hobbit") # Falha (não encontrado)

biblioteca_municipal.listar_catalogo()

# Teste de devolução
biblioteca_municipal.devolver_livro("1984") # Sucesso
biblioteca_municipal.devolver_livro("Dom Casmurro") # Falha (já disponível)

biblioteca_municipal.listar_catalogo()