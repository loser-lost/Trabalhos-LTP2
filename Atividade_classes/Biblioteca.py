class Biblioteca:
  
  tipo = "room"
  n_livros = 90

  def __init__(self, funcionarios, estantes):
    self.funcionarios = funcionarios
    self.estantes = estantes 

  def visao_geral(self):
    return f"Funcionários: {self.funcionarios}, Número de estantes na biblioteca: {self.estantes}"
  
  def emprestar(self):
    if self.n_livros > 0:
      self.n_livros = self.n_livros-1
      print("Livro emprestado com sucesso!")
    else:
      print("Não há livros disponíveis para empréstimo.")

  def receber(self):
    self.n_livros = self.n_livros+1
    return self.n_livros
    print("Livro devolvido com sucesso!")