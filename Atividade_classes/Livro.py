class Livro:
  TIPO = "book"
  STATUS_DISPONIVEL = 1
  STATUS_INDISPONIVEL = 0

  def __init__(self, titulo, autor, ano):
    self._titulo = titulo
    self._autor = autor
    self._ano = ano
    self._status = Livro.STATUS_DISPONIVEL

  def pegar(self):
    return f"{self._titulo},{self._autor},{self._ano}"
  
  def emprestar(self):
    if self._status == Livro.STATUS_DISPONIVEL:
      self._status = Livro.STATUS_INDISPONIVEL 
      print("disponível")
    else:
      print("indisponível")

  def devolver(self):
    if self._status == Livro.STATUS_INDISPONIVEL:
      self._status = Livro.STATUS_DISPONIVEL
      print("devolvido")