import re
import jwt
import datetime
#importando o pacote re que sera util na validação do email.


class User:
    #criando a classe user e definindo suas variaveis
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    
    #função de cadastro.
    def cadastrousUario(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
        # regex dara os paramatros para a verificação do email.
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, self.email)):
            #verifica se a senha atende aos criterios para ser cadastrada, caso seja cadastrara no banco de dados.
            if (self.senha.islower() and len(self.senha) < 7 and self.senha.isalpha() and self.senha.isalnum()):
                #cursor.execute("INSERT INTO user VALUES (self.nome, self.email, self.senha)")
            else:
                print("senha incorreta")          
        else:  
            print("email invalido")

    

        # define a chave secreta para a geração de tokens
        SECRET_KEY = 'minha_chave_secreta'

        # define o tempo de expiração do token (em minutos)
        EXPIRATION_MINUTES = 30

        # define a função para gerar um token de autenticação para um usuário
        def generate_token(user_id):
            payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRATION_MINUTES)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return token.decode('utf-8')


    #def loginUsuario(self, email, senha):
        #user = cursor.execute("SELECT * FROM user WHERE self.email = %s AND self.senha = %s" AND user_id, (email, senha))
    #    if(user > 1):
     #       generate_token()



              
            


      
 
  
    
    
    