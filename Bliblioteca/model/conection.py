#import mysql.connector

# Configurações de conexão com o banco de dados
config = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'database': 'nome_do_banco_de_dados'
}

# Conecta ao banco de dados
#conn = mysql.connector.connect(**config)

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Executa um comando SQL para criar uma tabela
cursor.execute('CREATE TABLE exemplo (id INT, nome VARCHAR(50))')

# Executa um comando SQL para inserir dados na tabela
cursor.execute("INSERT INTO exemplo VALUES (1, 'João')")
cursor.execute("INSERT INTO exemplo VALUES (2, 'Maria')")

# Faz um commit da transação (é necessário para gravar as alterações no banco de dados)
#conn.commit()

# Executa um comando SQL para selecionar os dados da tabela
cursor.execute('SELECT * FROM exemplo')

# Exibe os dados selecionados
for linha in cursor:
    print(linha)

# Fecha o cursor e a conexão
cursor.close()
#conn.close()