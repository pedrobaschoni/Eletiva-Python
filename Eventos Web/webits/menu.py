from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/tela1')
def tela1():
    return render_template('tela1.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/mostradados', methods=['POST', 'GET'])
def mostrar():
    if request.method == 'POST':
        result = request.form
        print(result)
        dados=[]
        dados.append(result['nome'])

        evento = {}
        evento['Nome:'] = result['nome']
        evento['Horario Inicio:'] = result['horarioinicio']
        evento['Horario Termino:'] = result['horariotermino']
        evento['Data:'] = result['data']

    return render_template("mostradados.html",result=evento)

import sys

if __name__ == '__main__':
    app.run(debug=True)


