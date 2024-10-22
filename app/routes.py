from app import app
from flask import render_template


@app.route('/index') # definindo uma rota para url do portal
#@app.route('/index', defaults={"nome":"usuario"})
#@app.route('/index/<nome>') # criando uma rota alternativa index para url do portal
def index():
    nome = 'Flavio'
    dados = {"profissao": "Analista Desenvolvedor","Nivel": "Senior"} 
    return render_template('index.html',nome= nome, dados= dados) # usando a função render_template para abrir arquivo html externo

@app.route('/contato') # definindo uma rota para url do portal
def contato():
    return render_template('contato.html') # usando a função render_template para abrir arquivo html externo

@app.route('/login') # definindo uma rota para url do portal
def login():
    return render_template('login.html')