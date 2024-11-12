from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculo', methods=['POST'])
def calcular():
    try:
        energia_referencia = float(request.form['energiaReferencia'])
        fator_emissao = float(request.form['fatorEmissao'])/100
        energia_projeto = float(request.form['energiaProjeto'])
        fator_emissao_projeto = float(request.form['fatorEmissaoProjeto'])/100

        emissao_referencia = energia_referencia * fator_emissao
        emissao_projeto = energia_projeto * fator_emissao_projeto
        reducao_emissoes = emissao_referencia - emissao_projeto

        return render_template('index.html', resultado=reducao_emissoes)

    except ValueError:
        return render_template('index.html', resultado="Erro nos valores inseridos.")
if __name__ == '__main__':
    app.run(debug=True)
