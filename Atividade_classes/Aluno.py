class Aluno:
  def __init__(self, nome, id, notas, book):
    self._nome = nome
    self._id = id
    self._notas = notas
    self._book = book

  def aluno_informacao(self):
    return f"{self._nome}, {self._id}, {self._notas}, {self._book}"
  
  def pegar_livro(self):
    self._book += 1
   
    
  def devolver(self):
    self._book -= 1
    return print(f"{self.book}")
    
    