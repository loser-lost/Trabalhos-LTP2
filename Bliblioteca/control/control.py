from model.User import User
from view import login
from flask import Flask

app = Flask(__name__)

#-------------------------------ROTAS DE Links--------------------------------------------------------------#

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/paglogin')
def pag_login():
    return render_template('login.html')

@app.rout('/pagcadastro')
def pag_cadastro():
    return render-template('cadastro.html')



#-------------------------------ROTAS DE FUNÇOES--------------------------------------------------------------#



cadastrar_usuario

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Passa as informações de login para o controlador
        resultado = controlador_de_login(username, password)
        return resultado
    else:
        return render_template('login.html')



#@app.route('/contact')
#def contact():
 #   return 'This is the contact page.'

#if __name__ == '__main__':
    #app.run(debug=True)
