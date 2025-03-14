from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_ENDPOINT = f'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    resultado = request.form.get('resultado', None)

    if not resultado: #vazio
        return render_template('index.html', erro="Você precisa informar um nome!")

    response = requests.get(API_ENDPOINT + resultado)

    if response.status_code == 200:
        data = response.json()
        url_imagem = data['data']['image']
        nome = data['data']['name']
        return render_template('index.html', resultado=resultado, url_imagem=url_imagem, nome=nome)
    elif response.status_code == 404:
        print(response.status_code)
        return render_template('index.html', erro404="Erro 404, busca não encontrada!")
    else:
        print(response.status_code)
        return render_template('index.html', erro="Erro no sistema!")

    


if __name__ == '__main__':
    app.run(debug=True)