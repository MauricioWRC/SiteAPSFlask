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
        # Energia em MWh e fator de emissão em gCO₂e/kWh (mesma unidade dos cards)
        energia_referencia = float(request.form['energiaReferencia'])
        fator_emissao = float(request.form['fatorEmissao'])
        energia_projeto = float(request.form['energiaProjeto'])
        fator_emissao_projeto = float(request.form['fatorEmissaoProjeto'])

        # MWh x gCO₂e/kWh / 1000 = toneladas de CO₂
        emissao_referencia = energia_referencia * fator_emissao / 1000
        emissao_projeto = energia_projeto * fator_emissao_projeto / 1000
        reducao_emissoes = emissao_referencia - emissao_projeto

        return render_template('index.html', resultado=round(reducao_emissoes, 2))

    except ValueError:
        return render_template('index.html', erro="Erro nos valores inseridos.")

if __name__ == '__main__':
    app.run(debug=True)
