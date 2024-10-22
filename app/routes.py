from app import app
from flask import render_template


@app.route('/') # definindo uma rota para url do portal
@app.route('/index/<nome>',defaults="nome":"usuario") # criando uma rota alternativa index para url do portal
def index(nome):
    dados = {"profissao": "Analista Desenvolvedor","Nivel": "Senior"} 
    return render_template('index.html',nome= nome, dados= dados) # usando a função render_template para abrir arquivo html externo

@app.route('/contato') # definindo uma rota para url do portal
def contato():
    return render_template('contato.html') # usando a função render_template para abrir arquivo html externo