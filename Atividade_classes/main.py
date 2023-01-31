from Aluno import Aluno
from Livro import Livro
from Biblioteca import Biblioteca

a_a = Aluno("Carlos", 1234, 6,6)
a_b = Aluno("Lucas", 2324, 9, 8)

print(a_a.aluno_informacao())
(a_a.pegar_livro())

l_a = Livro("Cronicas de narnia","Gerat",2008)
l_b = Livro("Cidades de papel", "jhon green",2013)

print(l_a.pegar()) 
(l_a.emprestar())

b_a = Biblioteca("Carlos", 4)
b_b = Biblioteca ("luci", 9)

print(b_a.visao_geral())
print(b_a.receber())

