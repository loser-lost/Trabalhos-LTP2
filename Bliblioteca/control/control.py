from model.User import User
from view import login
from flask import Flask, render_template, render_template_string, request, template_rendered

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
    return render_template_string-template_rendered('cadastro.html')



#-------------------------------ROTAS DE FUNÇOES--------------------------------------------------------------#



#cadastrar_usuario

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Passa as informações de login para o controlador
        resultado = loginUsuario(username, password)
        return resultado
    else:
        return render_template('login.html')



#@app.route('/contact')
#def contact():
 #   return 'This is the contact page.'

#if __name__ == '__main__':
    #app.run(debug=True)
