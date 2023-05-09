import mysql.connector

def connect():
    config = {
        'user': 'seu_usuario',
        'password': 'sua_senha',
        'host': 'localhost',
        'database': 'seu_banco_de_dados',
        'raise_on_warnings': True,
    }
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
